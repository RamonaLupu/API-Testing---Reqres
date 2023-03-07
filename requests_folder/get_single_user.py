import requests

def get_single_user():
    r = requests.get('https://reqres.in/api/users/2')
    return r