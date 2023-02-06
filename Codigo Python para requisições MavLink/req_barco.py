import requests

url = 'http://127.0.0.1:8000'  # api craida no fastapi

response = requests.get(url)

# try cath para uma requisiçãp se for truem barco do motor vai ligar, caso for false barco do motor vai desligar

try:
    if response.status_code == 200:
        data = response.json()
        print(data)
        print('Motor di Barco Ligado!')
    else:
        print('Motor do Barco desligando...')

except:
    print('Erro na requisição')
