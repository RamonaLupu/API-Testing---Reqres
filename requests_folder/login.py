import requests

def login(mail,pas):
    request_body = {
        "email": mail,
        "password": pas
    }
    r = requests.post('https://reqres.in/api/login', json=request_body)
    return r