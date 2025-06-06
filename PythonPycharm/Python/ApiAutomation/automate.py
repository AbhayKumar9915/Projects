import requests
import json

# base url defined as global(common), so can be used for all four functions
base_url = 'https://reqres.in'


# GET request function
def GET_Req():
    # first print in all functions is used for separating output for all for request results
    print("___GET___")
    # Adding params argument
    value = {'page': 2}
    # response object for storing response from GET request
    response = requests.get(url=base_url + '/api/users?', params=value, verify=False)
    # printing status code in console
    print('Status Code: ', response.status_code)
    ''' printing response(List of Users) in console by using json module, and used dumps method for 
    printing it in json format with proper indentation'''
    print(json.dumps(response.json(), indent=4))


# POST request function
def POST_Req():
    print("\n\n___POST___")
    # Data to add in database
    post_payload = {
        "name": "Abhay",
        "job": "Software Engineer"
    }
    # response object for storing response from POST request
    response = requests.post(url=base_url + '/api/users', data=post_payload, verify=False)
    print('Status Code: ', response.status_code)
    print(json.dumps(response.json(), indent=4))


# PUT request function
def PUT_Req():
    print("\n\n___PUT___")
    put_payload = {
        "name": "Ravi",
        "job": "Developer"
    }
    # response object for storing response from PUT request
    response = requests.put(url=base_url + '/api/users/2', data=put_payload, verify=False)
    print('Status Code: ', response.status_code)
    print(json.dumps(response.json(), indent=4))


# DELETE request function
def DELETE_Req():
    print("\n\n___DELETE___")
    # response object for storing response from DELETE request
    response = requests.delete(url=base_url + '/api/users/2', verify=False)
    print('Status Code: ', response.status_code)


# Calling all four function
GET_Req()
POST_Req()
PUT_Req()
DELETE_Req()
