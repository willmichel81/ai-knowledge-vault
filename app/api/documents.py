
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.document import Document, DocumentCreate
from app.services import documents

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.post("", response_model=Document, status_code=201)
def create_document(
    document: DocumentCreate,
    db: Annotated[Session, Depends(get_db)],
):
    return documents.create(db, document)

@router.get("/", response_model=list[Document])
def list_documents(
    db: Annotated[Session, Depends(get_db)],
):
    """List all documents."""
    return documents.list_documents(db)

@router.get("/{document_id}", response_model=Document)
def get_document(
    document_id: UUID,
    db: Annotated[Session, Depends(get_db)],
):
    """Get a document by its ID."""
    document = documents.get(db, document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document