import datetime
import random
import string
import uuid

import requests
from flask import Flask, request, jsonify, render_template, json, redirect, url_for

import Constants
import Utils
from Pages import home, reload, password, Clock
import sys

# import pycountry

def sizeof_string_in_bytes(string):
    return sys.getsizeof(string)

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


@app.route('/echo', methods=['POST', 'PUT', 'GET', 'PATCH', 'DELETE'])
# @app.route('/webhook', methods=['POST', 'PUT', 'GET', 'PATCH', 'DELETE'])
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


webhook_data = {}

@app.route('/webhooks/<key>', methods=['POST', 'PUT', 'GET', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS'])
def receive_webhook(key):

    method = request.method
    data = request.data.decode('utf-8')

    # Get current date and time
    current_time = datetime.datetime.now()
    # Format the date and time in a different style
    formatted_time = current_time.strftime("%A, %B %d, %Y %I:%M:%S %p")
    response = {
            "time": formatted_time,
            "method": method,
            "body": data
    }


    size_in_bytes = sizeof_string_in_bytes(response)

    if (size_in_bytes > 500):
        response = {
            "time": formatted_time,
            "method": method,
            "body": "Webhook is very Large. Size: " + str(size_in_bytes) + "bytes. DISCARDED"
        }

    if key not in webhook_data:
        webhook_data[key] = []
    webhook_data[key].append(response)

    # link = request.url_root + "webhook-received/" + key
    return "Webhook received successfully, Size: " + str(size_in_bytes)  + " bytes."


@app.route('/webhook-received', methods=['GET'])
def handle_webhook():
    # Generate a random UUID
    key = str(uuid.uuid4())
    webhook_data[key] = []
    # Redirect to the /webhook-received endpoint with the generated key
    return redirect(url_for('display_webhooks', key=key))


@app.route('/mac-address', methods=['GET']) # R&D needed
def get_mac_address():
    mac = uuid.getnode()
    mac_address = ':'.join(['{:02x}'.format((mac >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    return jsonify(mac_address)


refresh_time = "5"  # Default value 5 seconds
refresh_map = {}

@app.route('/webhook-received/<key>', methods=['GET'])
def display_webhooks(key):
    base_url = request.url_root
    webhooks_url = base_url + "webhooks/" + key

    if key not in webhook_data:
        webhook_data[key] = []
    if key not in refresh_map:
        refresh_map[key] = refresh_time

    mapKey = key

    return render_template('webhooks.html', mapKey=mapKey, refresh_content=refresh_map[key], key=webhooks_url, responses=webhook_data[key])


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_data = ''.join(random.choice(characters) for _ in range(length))
    return password_data


@app.route('/generate_password', methods=['GET'])
def get_random_password():
    length = int(request.args.get('length', 12))  # Default length is 12 characters
    password = generate_password(length)
    return jsonify({"password": password})


@app.route('/remove_refresh', methods=['POST'])
def remove_refresh():
    key = request.form.get('key')
    refresh_map[key] = None;
    return redirect(url_for('display_webhooks', key=key))


@app.route('/enable_refresh', methods=['POST'])
def enable_refresh():
    key = request.form.get('key')
    refresh_map[key] = refresh_time;
    return redirect(url_for('display_webhooks', key=key))

if __name__ == '__main__':
    app.run(debug=True)