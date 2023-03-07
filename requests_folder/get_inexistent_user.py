import requests

def get_inexistent_user():
    r = requests.get('https://reqres.in/api/users/23')
    return r