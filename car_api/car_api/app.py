# Importa a classe principal FastAPI da biblioteca que você instalou
from fastapi import FastAPI, status
from car_api.routers import users

# Cria a instância da aplicação (o "coração" da API) e a guarda na variável 'app'
app = FastAPI()

app.include_router(
    router=users.router,
    prefix='/api/v1/users',
    tags=['users'],
)

# Decorador que avisa a API: "Se receber uma requisição GET na raiz ('/'), rode a função abaixo"
@app.get('/health_check', status_code=status.HTTP_200_OK)
# Define a função Python que vai processar o pedido feito para essa rota
def health_check():
    # Retorna um dicionário que o FastAPI converte automaticamente para JSON antes de enviar ao usuário
    return {'status': 'OK!'}