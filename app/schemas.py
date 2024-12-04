from pydantic import BaseModel
from typing import List


class Movie(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class Suggestion(BaseModel):
    suggestions: List[Movie]


class Genres(BaseModel):
    genres: List[str]
