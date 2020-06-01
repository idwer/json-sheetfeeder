# source: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request

app = Flask(__name__)

# this was found at https://dev.to/rosejcday/setting-up-python-to-connect-to-google-sheets-2ak7
scope = ['https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("frank_api").sheet1

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        req_data = request.get_json(force = True)

        ev = req_data['ev']
        online = req_data['online']
        timestamp = req_data['timestamp']

        return ''
    elif request.method == 'GET':
        return "usage: curl -d '{ \"ev\" : \"ev01\", \"online\" : 0, \"timestamp\" : 1234567890}' http://127.0.0.1:5000/"

if __name__ == "__main__":
    app.run(debug=True)
