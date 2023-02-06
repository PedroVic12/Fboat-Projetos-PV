import requests

print('ola mundo')

reques = requests.get('http://127.0.0.1:8000/', auth=('user', 'pass'))
print(reques.text)
print(reques.json())
