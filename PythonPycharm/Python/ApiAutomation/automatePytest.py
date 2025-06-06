import requests
import json

# base url defined as global(common), so can be used for all four functions
base_url = 'https://reqres.in'


def test_GET_Req():
    value = {'page': 2}
    # response object for storing response from GET request
    response = requests.get(url=base_url + '/api/users?', params=value, verify=False)
    # printing status code in console
    print('Status Code for GET Request: ', response.status_code)
    ''' printing response(List of Users) in console by using json module, and used dumps method for
        printing it in json format with proper indentation'''
    print(json.dumps(response.json(), indent=4))
    # response_body object for storing values of body in json format
    response_body = response.json()
    # Validations
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert response_body['data'][0]['first_name'] == 'Michael'


def test_GET_Req_ByID():
    value = {'id': 2}
    response = requests.get(url=base_url + '/api/users/', params=value, verify=False)
    print('Status Code for GET Request: ', response.status_code)
    print(json.dumps(response.json(), indent=4))
    response_body = response.json()
    # Validation
    assert response.status_code == 200
    assert response.headers['connection'] == 'keep-alive'
    assert response_body['data']['first_name'] == 'Janet'


def test_POST_Req():
    # Add new data in database
    post_payload = {
        "name": "Abhay",
        "job": "Software Engineer"
    }
    # response object for storing response from POST request
    response = requests.post(url=base_url + '/api/users', data=post_payload, verify=False)
    print('Status Code for POST Request: ', response.status_code)
    print(json.dumps(response.json(), indent=4))
    # Validation
    assert response.status_code == 201


def test_PUT_Req():
    # Update/modify existing data in database
    put_payload = {
        "name": "Ravi",
        "job": "Developer"
    }
    # response object for storing response from PUT request
    response = requests.put(url=base_url + '/api/users/2', data=put_payload, verify=False)
    print('Status Code for PUT Request: ', response.status_code)
    print(json.dumps(response.json(), indent=4))
    # Validation
    assert response.status_code == 200


def test_DELETE_Req():
    # Delete existing data in database
    value = {'id': 2}
    response = requests.delete(url=base_url + '/api/users/', params=value, verify=False)
    print('Status Code for Delete Request: ', response.status_code)
    # Validation
    assert response.status_code == 204
