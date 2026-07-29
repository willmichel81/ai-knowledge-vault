from uuid import UUID, uuid4
from sqlalchemy.orm import Session

from app.database.models import DocumentModel
from app.schemas.document import Document, DocumentCreate

def create(db: Session, document: DocumentCreate) -> Document:
    db_document = DocumentModel(
        id=str(uuid4()),
        title=document.title,
        content=document.content,
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return Document(
        id=UUID(db_document.id),
        title=db_document.title,
        content=db_document.content,
    )

def list_documents(db: Session) -> list[Document]:
    rows = db.query(DocumentModel).all()

    return [
        Document(
            id=UUID(row.id),
            title=row.title,
            content=row.content,
        )
        for row in rows
    ]

def get(db: Session, document_id: UUID) -> Document | None:
    row = (
        db.query(DocumentModel)
        .filter(DocumentModel.id == str(document_id))
        .first()
    )

    if row is None:
        return None

    return Document(
        id=UUID(row.id),
        title=row.title,
        content=row.content,
    )