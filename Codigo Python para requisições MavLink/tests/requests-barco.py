import requests
import time


def fazendoRequisicao(url_request):
    response1 = requests.get(url_request)
    return response1


def conectandoMavlink():
    # TODO Cria uma conexão MAVLink em modo leitura (comport)
    pass


def consoleLog(txt):
    print('\n=========================')
    print(txt)
    print('=========================\n')


def pegandoDadosBarco(requisicao):
    try:
        if requisicao.status_code == 200:
            print(requisicao.status_code)
            data = requisicao.json()
            print(data)
            consoleLog('Motor do Barco Ligado!')

        else:
            consoleLog('Motor do Barco desligando...')
    except:
        print('Erro na requisição')


if __name__ == '__main__':

    # TODO tentar fazer 3 requisições ao mesmo tempo
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

    # Conectando com  a API do Google
    url_request = "https://maps.googleapis.com/maps/api/geocode/json"
    parametros = {'address': '1600 Amphitheatre Parkway, Mountain View, CA',
                  'key': 'SUA_CHAVE_API'}

    #! Conectando com minha proria api da fastApi
    url = 'http://127.0.0.1:8000/'
    time.sleep(2)

    # Testando conexão
    try:
        req = fazendoRequisicao(url)
        pegandoDadosBarco(req)
        # TODO COmo fazer requisição de uma resposta do Mavlink?

    except:
        print('Erro na requisição')
