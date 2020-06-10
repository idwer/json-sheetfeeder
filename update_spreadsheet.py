# source: https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

import credentials

import gspread

from datetime import datetime

worksheet_ready = False

def update_spreadsheet(key, online):
    global worksheet_ready

    if worksheet_ready is False:
        credentials.send_credentials()
        worksheet_ready = True

    worksheet = credentials.get_worksheet(credentials.send_credentials())

    try:
        # look up the key
        cell = worksheet.find(key)
        # when receiving non-key data through POST, check whether data in a cell needs updating
        # toggle 'status'
        if worksheet.acell(f'B{cell.row}') != online:
            worksheet.update(f'B{cell.row}', online)
        # overwrite timestamp
        timestamp = f"{datetime.now()}"
        worksheet.update(f'C{cell.row}', f"{timestamp}")

        return f'{key, online, timestamp}'

    # when the cell being looked up isn't found: insert data
    except gspread.exceptions.CellNotFound:
        return write_cell(worksheet, key, online, f"{datetime.now()}")

    return write_cell(worksheet, key, online, f"{datetime.now()}")

def write_cell(worksheet, key, online, timestamp):

    row_count = len(worksheet.col_values(1))

    worksheet.update_cell(row_count + 1, 1, key)
    worksheet.update_cell(row_count + 1, 2, online)
    worksheet.update_cell(row_count + 1, 3, timestamp)

    return f'{key, online, timestamp}'
