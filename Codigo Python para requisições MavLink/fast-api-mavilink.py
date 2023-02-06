from fastapi import FastAPI
import requests
from pymavlink import mavutil

app = FastAPI()

# Cria uma conexão MAVLink em modo leitura (comport)
master = mavutil.mavlink_connection('comport', baud=115200, source_system=255)


@app.get("/")
async def root():
    print('Script no terminal,uvicorn main:app --reload  ,executado com sucesso ')

    # Espera por uma mensagem HEARTBEAT
    msg = master.recv_match(type='HEARTBEAT', blocking=True)

    # Extrai informações da mensagem HEARTBEAT
    flight_mode = msg.custom_mode
    battery_voltage = msg.voltage_battery

    # Envia as informações para o servidor via requisição HTTP
    data = {
        'flight_mode': flight_mode,
        'battery_voltage': battery_voltage
    }
    response = requests.post('http://example.com/data', data=data)

    return {"message": "Pedro Victor", 'idade': 24}


"""
Neste exemplo, criamos uma conexão MAVLink no início do código usando a função mavlink_connection. 
Em seguida, adicionamos a lógica MAVLink para a rota principal do aplicativo (/), 
que extrai informações de uma mensagem HEARTBEAT e as envia a um servidor usando uma requisição HTTP.
 Observe que você precisará substituir o URL http://example.com/data pelo endereço do seu servidor.
"""
