from uuid import UUID

from sqlalchemy.orm import Session

from app.repositories import documents as repository
from app.schemas.document import Document, DocumentCreate


def create(db: Session, document: DocumentCreate) -> Document:
    return repository.create(db, document)


def list_documents(db: Session):
    return repository.list_documents(db)


def get(db: Session, document_id: UUID) -> Document | None:
    return repository.get(db, document_id)