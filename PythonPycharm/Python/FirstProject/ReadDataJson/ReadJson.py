import json
with open('Data.txt', 'r') as rf:
    s = rf.read()
    book = json.loads(s)
    print(book['Abhay']['phone'])
    # all records
    for person in book:
        print(book[person]['address'])
