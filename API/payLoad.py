
from utilities.configurations import *
def add_book_payLoad(isbn):
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": "34556227",
        "author": "John foe"
    }
    return body

def build_payload_from_db(query):
    add_body = {}
    enter_query = get_query(query)
    add_body['name'] = enter_query[0]
    add_body['isbn'] = enter_query[1]
    add_body['aisle'] = enter_query[2]
    add_body['author'] = enter_query[3]
    return add_body