# source: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

import credentials
import json_handler

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def route_home():
    return "usage: curl -d '{ \"ev\" : \"ev01\", \"online\" : 0}' http://127.0.0.1:5000/api"

@app.route('/api', methods=['POST'])
def route_api():
    req_data = request.get_json(force=True)

    return f"inserted {json_handler.handle_json(req_data)}"

if __name__ == "__main__":
    app.run(debug=True)
