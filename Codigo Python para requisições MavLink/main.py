from fastapi import FastAPI
import random


#! Gerando uma requisição com a fastAPI

app = FastAPI()

# TODO Cria uma conexão MAVLink em modo leitura (comport)


@app.get("/")
async def root():
    print('Script no terminal, --> uvicorn main:app --reload')
    print('Aperte enter para ligar o motor do barco')
    return {"message": "Pedro Victor", 'idade': 24, 'status': 'Barco Ligado'}
