import requests

def get_list(id):
    r = requests.get(f'https://reqres.in/api/unknown?id={id}')
    return r