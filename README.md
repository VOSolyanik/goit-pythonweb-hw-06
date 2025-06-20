# goit-pythonweb-hw-06

## Setup

### 1. Install project dependencies

-  `poetry install`

### 2. Run local Postgres DB in Docker

- `docker run --name student-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres` where `mysecretpassword` is your custom password. Other params could be changed too.

### 3. Create .env file

- You need to create `.env` file from sample `.env.sample` and update according to your params in Docker command that runs Postgres instance

### 4. Run DB migrations

- `poetry run alembic upgrade head`

### 5. Run seeding

- `poetry run python seed.py` to fill DB with test data

### 6. Run

- `poetry run python main.py` to check `my_select.py` result