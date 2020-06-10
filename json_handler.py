import update_spreadsheet

def get_key(req_data):
    return req_data['ev']

def get_status(req_data):
    return req_data['online']

def handle_json(req_data):
    return update_spreadsheet.update_spreadsheet(get_key(req_data), get_status(req_data))
