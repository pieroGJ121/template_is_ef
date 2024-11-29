from pydantic import BaseModel
from typing import List

class Movie(BaseModel):
    id: int
    title: str
    genre: str

    class Config:
        orm_mode = True

class Suggestion(BaseModel):
    user_id: int
    suggestions: List[Movie]