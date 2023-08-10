import requests
from payLoad import *
from utilities.configurations import *
from utilities.resources import *

# ADD CONFIGURATION AND URLS

config = get_config()
post_url = config['API']['endpoint'] + ApiResources.addBook
delete_url = config['API']['endpoint'] + ApiResources.deleteBook
headers = {'Content-Type': 'application/json'}

# ADD BOOK

addbook_response = requests.post(post_url, json=add_book_payLoad("qwertytui"), headers=headers, )

print(addbook_response.json())

response_json = addbook_response.json()

bookId = response_json['ID']
print(bookId)

# DELETE BOOK

response_delete_book = requests.post(delete_url, json={
    "ID": bookId
}, headers=headers, )

assert response_delete_book.status_code == 200

res_json = response_delete_book.json()

print(res_json['msg'])

assert res_json['msg'] == "book is successfully deleted"
