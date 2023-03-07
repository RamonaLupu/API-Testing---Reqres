import requests

def create_user():
    request_body = {
        "name": "morpheus",
        "job": "leader"
    }
    r = requests.post('https://reqres.in/api/users', json=request_body)
    return r