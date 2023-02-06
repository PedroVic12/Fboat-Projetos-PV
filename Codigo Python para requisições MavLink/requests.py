import requests

print('ola mundo')

# TODO : Fazer 3 Requisições HTTP GET

reques = requests.get('http://127.0.0.1:8000/', auth=('user', 'pass'))
print(reques.text)
print(reques.json())
