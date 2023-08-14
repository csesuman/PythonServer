import random
import string

from flask import Flask, request, jsonify, render_template

import Constants
import requests
import pycountry



import Utils
from Pages import home, reload, password, Clock

app = Flask(__name__)


@app.route('/') # start home page
def hello_world():
    return home.home_view()


@app.route('/myip')
def my_ip():
    x_forwarded_for = request.headers.getlist("X-Forwarded-For")
    response = requests.get('http://ipinfo.io')
    data = response.json()

    if "error" in data:
        response = requests.get('https://ip-api.io/json')
        data = response.json()
        try:
            ip_address = data['ip']
            city = data['city']
            region = data['region_name']
            full_country_name = data['country_name']
            return Utils.html_view(ip_address, city, region, full_country_name)
        except AttributeError:
            pass

    else:
        try:
            ip_address = data['ip']
            city = data['city']
            region = data['region']
            country_code = data['country']
            country = pycountry.countries.get(alpha_2=country_code)
            full_country_name = country.name
            return Utils.html_view(ip_address, city, region, full_country_name)
        except AttributeError:
            pass


@app.route('/iplocation')
def get_public_ip_and_location():
    try:
        response = requests.get('http://ipinfo.io')
        data = response.json()

        ip_address = data['ip']
        location = data['city'] + ', ' + data['region'] + ', ' + data['country']

        return response.json()
    except Exception as e:
        return None, str(e)

@app.route('/new_password', methods=['GET'])
def get_random_password_page():
    return password.password_generate_view()


# https://raw.githubusercontent.com/eggert/tz/master/zone.tab # All Cities are here!!
@app.route('/clock', methods=['GET'])
def get_clock_page():
    return Clock.digital_clock_view()


@app.route('/echo', methods=['POST','GET'])
@app.route('/webhook', methods=['POST','PUT','GET','PATCH','DELETE'])
def webhook_echo_responder():
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


@app.route('/reload', methods=['GET'])
def call_self():
    global hit
    hit = hit + 1
    return reload.reload_view(hit)


@app.route('/details', methods=['GET', 'POST'])
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
