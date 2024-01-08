import requests

API_URL = 'https://reqres.in/api/users'

def test_create_user():
    #Test case to create new user
    data = {'name': 'John Doe', 'job': 'Engineer'}
    response = requests.post(API_URL, json=data)
    assert response.status_code == 201
    assert 'id' in response.json()

def test_get_user_list():
    #Test case to retrieve list user
    response = requests.get(API_URL)
    assert response.status_code == 200
    assert 'data' in response.json()
