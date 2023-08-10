import json

import requests

url = 'http://216.10.245.166/Library/GetBook.php'

response = requests.get(url,
             params={'AuthorName':'Rahul Shetty'},
             )

print(response.text)
# print(type(response.text))
#
# dic_response = json.loads(response.text)
# print(type(dic_response))

json_response = response.json()
print(type(json_response))

assert response.status_code == 200

# print(response.headers)

assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

for book in json_response:
    if book['isbn'] == 'BNO121320':
        print(book)
        break

expectedBook = {"book_name":"Learning Rest API with QA academy","isbn":"BNO121320","aisle":"227",}

assert book == expectedBook