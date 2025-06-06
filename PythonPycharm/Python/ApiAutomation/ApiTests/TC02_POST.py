import requests
import json

base_url = 'https://reqres.in'

payload = {
    "name": "Abhay",
    "job": "leader"
}

response = requests.post(base_url + '/api/users',data=payload, verify=False)

print(response.status_code)
print(json.dumps(response.json(),indent=4))




