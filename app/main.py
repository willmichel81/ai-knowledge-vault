from fastapi import FastAPI

from app.api.documents import router as documents_router
from app.api.routes import router

app = FastAPI(title="AI Knowledge Vault", version="0.1.0")

app.include_router(router)
app.include_router(documents_router)