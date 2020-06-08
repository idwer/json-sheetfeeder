# source: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# source: https://realpython.com/python-testing/
# source: https://rubikscode.net/2019/03/04/test-driven-development-tdd-with-python/
import configparser
import gspread
import unittest

from oauth2client.service_account import ServiceAccountCredentials

class TestSpreadsheet(unittest.TestCase):
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    config = configparser.ConfigParser()
    config.read('spreadsheet.config')

    sheet = client.open_by_key(config['spreadsheet']['url_key'])
    worksheet = sheet.worksheet(config['workspace']['sheet'])

    def test(self):
        self.assertTrue(self.sheet, "<Worksheet 'Sheet1' id:0>")

if __name__ == '__main__':
    unittest.main()
