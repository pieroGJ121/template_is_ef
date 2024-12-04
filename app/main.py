from fastapi import FastAPI, HTTPException, Depends
from app.database import engine, Base, get_db
from sqlalchemy.orm import Session
from app import crud
from app.schemas import Movie, Suggestion, Genres
from app.logger import logger

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Suggestion API", docs_url="/swagger")


@app.post("/suggestions/genre", response_model=Suggestion)
def get_suggestions_genre(genres: Genres, db: Session = Depends(get_db)):
    """Endpoint to suggest movies based on user preferences."""
    try:
        genres_list = genres.genres
        # Example: Return top 3 movies for each preferred genre
        suggestions = []
        for genre in genres_list:
            current = crud.get_movies_by_genre(db, genre)[:3]
            print(current)
            suggestions.extend(current)

        logger.info("Exito en ejecucion")
        print(suggestions)
        return {"suggestions": suggestions}
    except Exception as e:
        logger.error("Error en ejecucion")
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
