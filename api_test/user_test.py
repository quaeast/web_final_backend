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


def create_user():
    url = 'http://127.0.0.1:8000/logon/'
    users_response = requests.post(url, json={
        'username': 'wang',
        'email': '4@bjfu.com',
        'password': '1234'
    })
    return users_response


if __name__ == '__main__':
    print(create_user().content)
