import requests

url = 'https://www.example.com/api/endpoint'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Processar a resposta aqui
else:
    # Tratar erro aqui
