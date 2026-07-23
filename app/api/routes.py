from fastapi import APIRouter
from app.config import APP_NAME, VERSION, ENVIRONMENT
from app.logger import logger
import socket
import sys

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": "Welcome to AI Knowledge Vault"
    }

@router.get("/health")
def health():
    logger.info("Health endpoint called")

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

@router.get("/system")
def system_info():
    return {
        "application": "AI Knowledge Vault",
        "hostname": socket.gethostname(),
        "python_version": sys.version,
        "environment": ENVIRONMENT
    }