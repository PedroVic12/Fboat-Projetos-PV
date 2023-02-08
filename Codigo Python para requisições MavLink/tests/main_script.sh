echo 'Iniciando Script...'

echo 'Instalando as Depedencias...'
python3 install-depedences.py 
clear

echo 'Iniciando a minha propria API.'
python3 main.py

# & é usado para executar os codigos em paralelo
uvicorn main:app --reload &

echo 'Iniciando o meu script em Python de Requisição.'
python3 requests-barco.py &
