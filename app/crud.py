from sqlalchemy.orm import Session
from app.models import User, Preference, Movie

def get_user_preferences(db: Session, user_id: int):
    return db.query(Preference).filter(Preference.user_id == user_id).all()

def get_movies_by_genre(db: Session, genre: str):
    return db.query(Movie).filter(Movie.genre == genre).all()