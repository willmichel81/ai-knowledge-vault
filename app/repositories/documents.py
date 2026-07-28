from uuid import UUID

from app.schemas.document import Document, DocumentCreate

_documents: dict[UUID, Document] = {}


def create(document: DocumentCreate) -> Document:
    new_document = Document(**document.model_dump())
    _documents[new_document.id] = new_document
    return new_document


def list_documents() -> list[Document]:
    return list(_documents.values())


def get(document_id: UUID) -> Document | None:
    return _documents.get(document_id)