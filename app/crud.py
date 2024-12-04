from sqlalchemy.orm import Session
from app.models import Movie


def get_movies_by_genre(db: Session, genre: str):
    return db.query(Movie).filter(Movie.genre == genre).all()
