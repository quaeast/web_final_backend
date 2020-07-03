import requests
from api_test.jwt_test import get_token


def get_student(token):
    url = 'http://127.0.0.1:8000/student/'
    headers = {'Authorization': 'JWT ' + token}
    student_response = requests.get(url, headers=headers)
    return student_response


def post_student(token):
    url = 'http://127.0.0.1:8000/student/'
    headers = {'Authorization': 'JWT ' + token}
    student_response = requests.post(
        url,
        headers=headers,
        json={'name': 'fangzidong', 'schoolId': '171002312'})
    return student_response


if __name__ == '__main__':
    print(post_student(get_token()).content)
    # print(get_student(get_token()).content)
