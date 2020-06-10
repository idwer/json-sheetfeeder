import configparser
import gspread

from oauth2client.service_account import ServiceAccountCredentials

def send_credentials():
# this was found at https://dev.to/rosejcday/setting-up-python-to-connect-to-google-sheets-2ak7
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    return gspread.authorize(creds)

def get_worksheet(client):
    config = configparser.ConfigParser()
    config.read('spreadsheet.config')

    sheet = client.open_by_key(config['spreadsheet']['url_key'])
    worksheet = sheet.worksheet(config['workspace']['sheet'])

    return worksheet
