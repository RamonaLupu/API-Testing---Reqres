import requests

def delete_user():
    r = requests.delete('https://reqres.in/api/users/2')
    return r