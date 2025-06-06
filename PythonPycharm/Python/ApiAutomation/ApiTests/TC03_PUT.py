import requests
import json

base_url = 'https://reqres.in'

payload = {
    "name": "David",
    "job": "zion resident"
}

response = requests.put(base_url + '/api/users/2',data=payload, verify=False)

print(response.status_code)
print(json.dumps(response.json(),indent=4))




