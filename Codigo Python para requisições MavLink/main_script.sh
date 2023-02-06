echo 'Iniciando Script...'

echo 'Instalando as Depedencias...'

echo 'Iniciando a minha propria API.'
# & é usado para executar os codigos em paralelo
uvicorn main:app --reload &


echo 'Iniciando o meu script em Python de Requisição.'
python3 requests-barco.py &
