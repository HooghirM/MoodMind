from pydantic import BaseModel


class EntryCreate(BaseModel):
    user_id: int
    content: str

class EntryRead(BaseModel):
    id: int
    user_id: int
    content: str
    created_at: str