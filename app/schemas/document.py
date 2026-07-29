from uuid import UUID

from pydantic import BaseModel


class DocumentCreate(BaseModel):
    title: str
    content: str


class Document(BaseModel):
    id: UUID
    title: str
    content: str