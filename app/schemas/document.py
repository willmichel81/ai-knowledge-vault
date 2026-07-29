from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class DocumentCreate(BaseModel):
    title: str
    content: str


class Document(BaseModel):
    id: UUID
    title: str
    content: str