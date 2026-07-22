from fastapi import APIRouter
from app.config import APP_NAME, VERSION, ENVIRONMENT

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": "Welcome to AI Knowledge Vault"
    }

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }

@router.get("/info")
def info():
    return {
        "name": APP_NAME,
        "version": VERSION,
        "environment": ENVIRONMENT
    }