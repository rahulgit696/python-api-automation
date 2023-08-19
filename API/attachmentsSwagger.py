import requests

# headers = {'Content-Type': 'image/png'}
url = 'https://petstore3.swagger.io/api/v3/pet/1232123/uploadImage'
files = {'file': open(r"C:\Users\Rahul Badoni\Downloads\AdharCard.png", 'rb')}


headers = {
    'Content-Type': 'image/png',  # Replace with the correct content type
    'Content-Disposition': 'attachment; filename="AdharCard.png"'
}
attach_response = requests.post(url, files=files, headers=headers)
print(attach_response.status_code)
print(attach_response.text)