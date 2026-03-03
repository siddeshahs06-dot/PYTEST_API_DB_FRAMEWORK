import requests

def get_user(base_url, user_id):

    url = f"{base_url}/users/{user_id}"
    response = requests.get(url)

    return response
