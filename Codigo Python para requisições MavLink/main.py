from fastapi import FastAPI
import random


#! Gerando uma requisição com a fastAPI

app = FastAPI()

# Cria uma conexão MAVLink em modo leitura (comport)

@app.get("/")
async def root():
    print('Script no terminal,uvicorn main:app --reload  ,executado com sucesso ')
    return {"message": "Pedro Victor", 'idade': 24}
