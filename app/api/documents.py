from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas.document import Document, DocumentCreate
from app.services import document_service

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.post("/", response_model=Document, status_code=201)
def create_document(document: DocumentCreate):
    """Create a new document."""
    return document_service.create(document)

@router.get("/", response_model=list[Document])
def list_documents():
    """List all documents."""
    return document_service.list_documents()

@router.get("/{document_id}", response_model=Document)
def get_document(document_id: UUID):
    """Get a document by its ID."""
    document = document_service.get(document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document