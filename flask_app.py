import time

from flask import Flask, request, jsonify, send_file, render_template

import urllib.request
# from flask import requests
import Utils
import random
import string
import time

from Pages import home, reload, password

app = Flask(__name__)


@app.route('/')
def hello_world():
    return home.home_view()


@app.route('/myip')
def my_ip():
    x_forwarded_for = request.headers.getlist("X-Forwarded-For")

    if x_forwarded_for:
        ip = x_forwarded_for[0]
        return Utils.html_view("Your Public IP: " + ip)
    else:
        return Utils.html_view("Sorry, can't detect your public IP.")


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@app.route('/generate_password', methods=['GET'])
def get_random_password():
    length = int(request.args.get('length', 12))  # Default length is 12 characters
    password = generate_password(length)
    return jsonify({"password": password})


@app.route('/new_password', methods=['GET'])
def get_random_password_page():
    return password.password_generate_view()


hit = 0


@app.route('/reload', methods=['GET'])
def call_self():
    global hit
    hit = hit + 1
    return reload.reload_view(hit)


@app.route('/get_file', methods=['GET'])
def get_file():
    # Specify the path to the file you want to send
    file_path = './index.html'

    # Read the contents of the file
    with open(file_path, 'r') as file:
        file_contents = file.read()

    return render_template('file_page.Pages', file_contents=file_contents)


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
    # password = headers.get('Password')
    #
    # if password != Constants.CORRECT_PASSWORD:
    #     return jsonify({"message": "Unauthorized: Invalid password"}), 401

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


if __name__ == '__main__':
    app.run(debug=True)
