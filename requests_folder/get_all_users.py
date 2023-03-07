import requests

def get_all_users():
    r = requests.get('https://reqres.in/api/users?page=2')
    return r