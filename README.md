# AI Knowledge Vault

FastAPI-based AI knowledge management service.

## Local Development

Create environment:

cp .env.example .env

Install dependencies:

pip install -r requirements.txt

Run:

uvicorn app.main:app --reload

## Docker

docker compose up --build