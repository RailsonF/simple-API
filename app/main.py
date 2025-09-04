#Importando o pacote do FasApi
from fastapi import FastAPI

#instanciando a classe ao nosso APP
app = FastAPI()

#Importando os arquivos das rotas
from .routes.health import health_router
from .routes.about import about_router

app.include_router(health_router)
app.include_router(about_router)

@app.router.get("/")
def home():
    return {"Olá:":"Seja Bem Vindo!!", "endpoints": "/health e /about"}