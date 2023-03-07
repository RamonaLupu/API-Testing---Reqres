import requests

def update_user():
    request_body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    r = requests.patch('https://reqres.in/api/users/2', json=request_body)
    return r