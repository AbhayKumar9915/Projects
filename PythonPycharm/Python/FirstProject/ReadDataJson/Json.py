book = {}

book['Abhay'] = {
    'name' : 'Abhay',
    'address' : 'Bengaluru',
    'phone' : 5456651
}

book['Ravi'] = {
    'name' : 'Ravi',
    'address' : 'Lucknow',
    'phone' : 156456
}

book['Ruchi'] = {
    'name' : 'Ruchi',
    'address' : 'Saharanpur',
    'phone' : 464641
}

import json

s = json.dumps(book,indent=4)

with open('Data.txt','w') as wf:
    wf.write(s)