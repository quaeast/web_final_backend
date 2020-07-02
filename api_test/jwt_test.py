import requests


def get_token():
    url = 'http://127.0.0.1:8000/api-token-auth/'
    user_info = {"username": "admin", "password": "fang"}
    login_response = requests.post(url, json=user_info)
    return login_response.json()['token']


def verify_token(token):
    url = 'http://localhost:8000/api-token-verify/'
    print(token)
    verify_response = requests.post(url, json={'token': token})
    return verify_response


def get_users(token):
    url = 'http://127.0.0.1:8000/users/'
    headers = {'Authorization': 'JWT ' + token}
    users_info = requests.get(url, headers=headers)
    return users_info


if __name__ == '__main__':
    print(verify_token(get_token()))
