import requests
import json

base_url = 'https://reqres.in'
#Adding params argument
param = {'page': 2}
response = requests.get(base_url + '/api/users?', params=param, verify=False)
# print(response.content)
print('Status Code: ',response.status_code)
#Getting response in more readeale format using json module
print(json.dumps(response.json(),indent=4))

res_body = response.json()
print(res_body['data'][1]['first_name'])

#Getting all same values using list comprehension
print([d['first_name'] for d in res_body['data']])