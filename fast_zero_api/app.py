from fastapi import FastAPI

app = FastAPI()  # Instancio o objeto FastAPI


# Definindo um endpoint com o endereço / acessível pelo método HTTP GET
@app.get('/')
def read_root():
    # return {'message': 'Olá Mundo'}
    msg = 'Estou na raiz, teste swagger/'
    return msg


# Replicando mais endpoints
@app.get('/comida')
def rango():
    msg = 'Estou no /comida'
    return msg


@app.get('/carro')
def carro():
    msg = 'Estou no /carro'
    return msg
