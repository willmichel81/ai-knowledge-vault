from fastapi import FastAPI

from app.api.documents import router as documents_router
from app.api.routes import router
from app.database.database import init_db

app = FastAPI(title="AI Knowledge Vault", version="0.1.0")
init_db()
app.include_router(router)
app.include_router(documents_router)