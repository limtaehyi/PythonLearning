import requests
import json

response = requests.get('https://api.example.com/data')
print(response.status_code)  # 응답 상태 코드
print(response.text)  # 응답 본문

params = {'key': 'value'}
response = requests.get('https://api.example.com/data', params=params)
print(response.text)

data = {'key': 'value'}
response = requests.post('https://api.example.com/submit', data=data)
print(response.status_code)
print(response.text)


data = {'key': 'value'}
headers = {'Content-Type': 'application/json'}
response = requests.post('https://api.example.com/submit', data=json.dumps(data), headers=headers)
print(response.text)

headers = {'Authorization': 'Bearer <access_token>'}
response = requests.get('https://api.example.com/data', headers=headers)
print(response.text)

files = {'file': open('path/to/file', 'rb')}
response = requests.post('https://api.example.com/upload', files=files)
print(response.text)

session = requests.Session()
session.get('https://api.example.com/login', params={'username': 'user', 'password': 'pass'})
response = session.get('https://api.example.com/data')
print(response.text)
