from pydantic import BaseModel


class DailySummaryRead(BaseModel):
    id: int
    user_id: int
    date: str
    average_score: float
    entry_count: int