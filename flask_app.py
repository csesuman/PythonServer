import datetime
import random
import string
import uuid

import requests
from flask import Flask, request, jsonify, render_template, json

import Constants
import Utils
from Pages import home, reload, password, Clock

# import pycountry

app = Flask(__name__)


@app.route('/')  # start home page
def hello_world():
    return home.home_view()


@app.route('/myip')# 1
def my_ip():
    x_forwarded_for = request.headers.getlist("X-Forwarded-For")
    ip = x_forwarded_for[0]
    url = f"http://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()

    try:
        ip_address = data['ip']
        city = data['city']
        region = data['region']
        country_code = data['country']
        # country = pycountry.countries.get(alpha_2=country_code) // fix it
        # full_country_name = country.name
        return Utils.html_view(ip_address, city, region, country_code)
    except AttributeError:
        pass


@app.route('/ipinformation') #2
def get_public_ip_and_location():
    try:
        response = requests.get('http://ipinfo.io')
        data = response.json()

        return response.json()
    except Exception as e:
        return None, str(e)


@app.route('/new_password', methods=['GET'])  #3 # password generator
def get_random_password_page():
    return password.password_generate_view()


# https://raw.githubusercontent.com/eggert/tz/master/zone.tab # All Cities are here!!
@app.route('/clock', methods=['GET']) #4
def get_clock_page():
    return Clock.digital_clock_view()


@app.route('/echo', methods=['POST', 'GET'])
@app.route('/webhook', methods=['POST', 'PUT', 'GET', 'PATCH', 'DELETE'])
def webhook_echo_responder(): #5  #Make the real one
    data = request.data.decode('utf-8')
    args = dict(request.args)
    form = dict(request.form)

    response = {
        "message": "Your request is received successfully :). Delivering to you as proof",
        "Request": {
            "Raw Data": data,
            "Query Parameters": args,
            "Form Data": form
        }
    }

    return jsonify(response)


hit = 0


@app.route('/reload', methods=['GET']) #6
def call_self():
    global hit
    hit = hit + 1
    return reload.reload_view(hit)


def internal_details():
    method = request.method
    url = request.url
    headers = dict(request.headers)
    data = request.data.decode('utf-8')
    args = dict(request.args)
    form = dict(request.form)
    # Verify the password

    response = {
        "message": "Request details fetched successfully!",
        "details": {
            "Request Method": method,
            "URL": url,
            "Headers": headers,
            "Raw Data": data,
            "Query Parameters": args,
            "Form Data": form
        }
    }

    return response


@app.route('/details', methods=['GET', 'POST']) #7 # Protected!!
def request_details():
    method = request.method
    url = request.url
    headers = dict(request.headers)
    data = request.data.decode('utf-8')
    args = dict(request.args)
    form = dict(request.form)
    # Verify the password

    # Extract the password from the request headers
    passkey = headers.get('Password')
    #
    if passkey != Constants.CORRECT_PASSWORD:
        return jsonify({"message": "Unauthorized: Invalid password"}), 401

    response = {
        "message": "Request details fetched successfully!",
        "details": {
            "Request Method": method,
            "URL": url,
            "Headers": headers,
            "Raw Data": data,
            "Query Parameters": args,
            "Form Data": form
        }
    }

    return jsonify(response)


@app.route('/index') #8
def index():
    details = internal_details()
    json_string = json.dumps(details)

    current_time = datetime.datetime.now()
    unique_id = uuid.uuid4()

    with open('saved_text.txt', 'a') as file:
        file.write(str(unique_id) + " >> " + str(current_time) + json_string + '\n')

    # return json_string
    return render_template('input_message.html', unique_id=unique_id)


@app.route('/save', methods=['POST']) #9
def save_text():
    try:
        data = request.get_json()
        text = data['text']

        with open('saved_text.txt', 'a') as file:
            file.write(text + '\n')

        return jsonify(message='Text saved to server successfully!')
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route('/make_request', methods=['POST'])
def make_request():
    try:
        data = request.get_json()
        url = data.get('url')
        request_type = data.get('request_type', 'GET')
        counter = data.get('counter', 1)

        if not url:
            return jsonify({'error': 'URL is required'}), 400

        response_data = []

        for _ in range(counter):
            if request_type.upper() == 'GET':
                response = requests.get(url)
            elif request_type.upper() == 'POST':
                response = requests.post(url)
            else:
                return jsonify({'error': 'Unsupported request type'}), 400

            response_info = {
                'status_code': response.status_code,
                'content': response.text
            }
            response_data.append(response_info)

        return jsonify(response_data), 200
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 500


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_data = ''.join(random.choice(characters) for _ in range(length))
    return password_data


@app.route('/generate_password', methods=['GET'])
def get_random_password():
    length = int(request.args.get('length', 12))  # Default length is 12 characters
    password = generate_password(length)
    return jsonify({"password": password})


if __name__ == '__main__':
    app.run(debug=True)
