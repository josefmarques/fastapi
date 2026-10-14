mkdir fast_master
cd fast_master/
poetry new --flat eletrosil_api
cd eletrosil_api/
poetry python install 3.14
poetry python list
poetry env use 3.14
poetry env info
poetry install (cria o poetry.lock e dependências)
poetry add 'fastapi[standard]'
poetry run fastapi dev car_api/app.py
poetry add "sqlalchemy[asyncio]
poetry add aiosqlite
poetry add pydantic-settings
poetry add alembic
source /home/zemarques/.cache/pypoetry/virtualenvs/car-api-EYUxc8Qa-py3.14/bin/activate
poetry run alembic init migrations
# gera as migrations
poetry run alembic revision --autogenerate -m "create users table"

# aplica as migrations no banco
poetry run alembic upgrade head

cd /home/zemarques/fastapi/car_api
poetry run fastapi dev car_api/app.py
# outra aba do terminal:
curl -X POST http://127.0.0.1:8000/api/v1/users/ \
  -H 'Content-Type: application/json' \
  -d '{"username":"maria","email":"maria@example.com","password":"abc"}'
sqlite3 car.db "SELECT * FROM users;"
