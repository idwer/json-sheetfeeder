# source: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# source: https://realpython.com/python-testing/
# source: https://rubikscode.net/2019/03/04/test-driven-development-tdd-with-python/

import spreadsheet
import unittest

class TestFlask(unittest.TestCase):
    def setUp(self):
        spreadsheet.app.testing = True
        self.app = spreadsheet.app.test_client()

    def test(self):
        result = self.app.get('/')
        self.assertTrue(result, "<Response streamed [200 OK]>")

if __name__ == '__main__':
    unittest.main()
