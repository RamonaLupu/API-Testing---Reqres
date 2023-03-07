import requests

def update():
    request_body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    r = requests.put('https://reqres.in/api/users/2', json=request_body)
    return r