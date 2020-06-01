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

@app.route('/', methods=['GET'])
def route_home():
    return "usage: curl -d '{ \"ev\" : \"ev01\", \"online\" : 0, \"timestamp\" : 1234567890}' http://127.0.0.1:5000/"

@app.route('/api', methods=['POST'])
def route_api():
    req_data = request.get_json(force = True)

    ev = req_data['ev']
    online = req_data['online']
    timestamp = req_data['timestamp']

    cell = ''

    try:
        # look up the value passed to 'ev'
        cell = sheet.find(ev)
        # when receiving non-key data through POST, check whether data in a cell needs updating:
        if sheet.acell(f'B{cell.row}') != online:
            sheet.update(f'B{cell.row}', online)
        if sheet.acell(f'C{cell.row}') != timestamp:
            sheet.update(f'C{cell.row}', timestamp)

        return f"{cell.row}"
    # when the cell being looked up isn't found: insert data
    except gspread.exceptions.CellNotFound:
        update_cell(sheet, ev, online, timestamp)

        return f"inserted {req_data}\n"

#def update_cell(ev, online, timestamp):
def update_cell(sheet, ev, online, timestamp):
    row_count = len(sheet.col_values(1))

    sheet.update_cell(row_count + 1, 1, ev)
    sheet.update_cell(row_count + 1, 2, online)
    sheet.update_cell(row_count + 1, 3, timestamp)

if __name__ == "__main__":
    app.run(debug=True)
