import requests

def register(mail,pas):
    request_body = {
        "email": mail,
        "password": pas
    }
    r = requests.post('https://reqres.in/api/register', json=request_body)
    return r