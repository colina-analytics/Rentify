import os, json

def get_user_data_by_id(user_id):
    return {
        'id': 1,
        'first_name': 'Tobias',
        'last_name': 'Benavides',
        'email': 'tobias.benavides@gmail.com',
        'password': '1234',
    }


def open_json(filepath, filename):
    with open(os.path.join(filepath, filename), 'r', encoding='UTF-8') as f:
        return json.load(f)
    

def get_user_data_by_email(email):
    return {
        'id': 1,
        'first_name': 'Tobias',
        'last_name': 'Benavides',
        'email': 'tobias.benavides@gmail.com',
        'password': '1234',
    }