import requests
import time

# API 1: Google Maps Geocoding API
url1 = "https://maps.googleapis.com/maps/api/geocode/json"
params1 = {'address': '1600 Amphitheatre Parkway, Mountain View, CA',
           'key': 'SUA_CHAVE_API'}

# API 2: Google Places API
url2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
params2 = {'location': '37.4219999,-122.0840575',
           'radius': '500', 'type': 'restaurant', 'key': 'SUA_CHAVE_API'}


# API 3: Google Distance Matrix API
url3 = "https://maps.googleapis.com/maps/api/distancematrix/json"
params3 = {'origins': 'Washington,DC',
           'destinations': 'New+York+City,NY', 'key': 'SUA_CHAVE'}


# def fazendoRequisicao(url_request, parametros):
#     response = requests.get(url_request, params=parametros)
#     my_data_request = response.json()
#     return my_data_request


def fazendoRequisicao(url_request):
    response1 = requests.get(url_request)
    return response1
    # my_data_request = response1.json()
    # return my_data_request

# try cath para uma requisiçãp se for truem barco do motor vai ligar, caso for false barco do motor vai desligar


def pegandoDadosBarco(requisicao):

    try:
        if requisicao.status_code == 200:
            print(requisicao.status_code)
            data = requisicao.json()
            print(data)
            print('Motor do Barco Ligado!')
        else:
            print('Motor do Barco desligando...')

    except:
        print('Erro na requisição')


def main():
    # Conectando com  a API do Google
    url_request = "https://maps.googleapis.com/maps/api/geocode/json"
    parametros = {'address': '1600 Amphitheatre Parkway, Mountain View, CA',
                  'key': 'SUA_CHAVE_API'}

    # Conectando com minha proria api
    url = 'http://127.0.0.1:8000/'

    time.sleep(2)
    req = fazendoRequisicao(url)
    pegandoDadosBarco(req)


main()
