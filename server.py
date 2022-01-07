# set up a flask server to serve in localhost:5000
from datetime import datetime
from flask import Flask, render_template, request, send_file, jsonify
import requests
import os
import random
import string
import json


app = Flask(__name__, template_folder=".")

# declare folder to save files from requests to the server (in this case, folder)
# (this is the folder where the files will be saved)
UPLOAD_FOLDER = "./uploads"
TEMPLATES = "./templates"


def template_path(template):
    return TEMPLATES + "/" + template


time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# create a session token to be used in the requests to the server
# (this is the token that will be used in the requests to the server)
secure_token = "yourdamntoken".join(
    random.choice(string.ascii_uppercase + string.digits) for _ in range(32)
)
session_token = "secure_token" + time_now


@app.after_request
def after_request(response):
    secure_token = "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(256)
    )
    session_token = secure_token + time_now
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST"),
    response.headers.add("X-Session-Token:", session_token)
    return response


@app.route("/url", methods=["GET", "POST"])
def send_url():
    if request.method == "POST":
        # get url from json object
        request_body = request.get_json()
        decoded_json = json.dumps(request_body)
        url = json.loads(decoded_json)["payload"]["url"]
        # send url to web_scanner
        from web_scanner import web_scanner

        ws = web_scanner(url).get_headers()
        print(ws)
        # # send ws back to the client
        return ws
    else:
        return "OK"


if __name__ == "__main__":
    app.run(debug=True, host="192.168.1.2", port=5000)
