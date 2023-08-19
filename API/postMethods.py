import requests

from API.payLoad import *
from utilities.configurations import *
from utilities.resources import ApiResources

# ADD CONFIGURATION AND URLS

config = get_config()
post_url = config['API']['endpoint'] + ApiResources.addBook
delete_url = config['API']['endpoint'] + ApiResources.deleteBook
headers = {'Content-Type': 'application/json'}
query = 'select * from Books'

# ADD BOOK

addbook_response = requests.post(post_url, json=build_payload_from_db(query), headers=headers, )

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

# SAMPLE AUTHENTICATION CHECK AND CREATING SESSION MANAGER

session = requests.session()
session.auth = auth = ('rahulgit696', get_password())
url = 'https://api.github.com/user'
git_response = requests.get(url, auth=('rahulgit696', get_password()))
print(git_response.status_code)

repo_url = 'https://api.github.com/user/repos'
response = session.get(repo_url)
print(response.status_code)