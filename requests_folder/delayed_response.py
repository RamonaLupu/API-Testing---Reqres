import requests

def delayed_response():
    r = requests.get('https://reqres.in/api/users?delay=3')
    return r