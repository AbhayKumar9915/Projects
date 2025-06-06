import requests
import json

base_url = 'https://reqres.in'

response = requests.delete(base_url + '/api/users/2', verify=False)

print(response.status_code)




