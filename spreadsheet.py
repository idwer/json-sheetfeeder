# source: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
import configparser
import gspread

from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request

app = Flask(__name__)

# this was found at https://dev.to/rosejcday/setting-up-python-to-connect-to-google-sheets-2ak7
scope = ['https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

config = configparser.ConfigParser()
config.read('spreadsheet.config')

sheet = client.open_by_key(config['spreadsheet']['url_key'])
worksheet = sheet.worksheet(config['workspace']['sheet'])

@app.route('/', methods=['GET'])
def route_home():
    return "usage: curl -d '{ \"ev\" : \"ev01\", \"online\" : 0}' http://127.0.0.1:5000/api"

@app.route('/api', methods=['POST'])
def route_api():
    req_data = request.get_json(force = True)

    ev = req_data['ev']
    online = req_data['online']

    timestamp = f"{datetime.now()}"

    cell = ''

    try:
        # look up the value passed to 'ev'
        cell = worksheet.find(ev)
        # when receiving non-key data through POST, check whether data in a cell needs updating
        # toggle 'online'
        if worksheet.acell(f'B{cell.row}') != online:
            worksheet.update(f'B{cell.row}', online)
        # overwrite timestamp
        worksheet.update(f'C{cell.row}', timestamp)

        return ''
    # when the cell being looked up isn't found: insert data
    except gspread.exceptions.CellNotFound:
        write_cell(worksheet, ev, online, timestamp)

        return f"inserted {req_data}"

def write_cell(worksheet, ev, online, timestamp):
    row_count = len(worksheet.col_values(1))

    worksheet.update_cell(row_count + 1, 1, ev)
    worksheet.update_cell(row_count + 1, 2, online)
    worksheet.update_cell(row_count + 1, 3, timestamp)

if __name__ == "__main__":
    app.run(debug=True)
