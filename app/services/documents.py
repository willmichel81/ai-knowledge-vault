from uuid import UUID

from app.repositories import documents as repository
from app.schemas.document import Document, DocumentCreate


def create(document: DocumentCreate) -> Document:
    return repository.create(document)


def list_documents() -> list[Document]:
    return repository.list_documents()


def get(document_id: UUID) -> Document | None:
    return repository.get(document_id)