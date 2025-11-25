from pydantic import BaseModel


class MoodScoreRead(BaseModel):
    id: int
    entry_id: int
    score: float
    label: str
    analyzed_at: str