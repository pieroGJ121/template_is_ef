from fastapi import FastAPI, HTTPException, Depends
from app.database import engine, Base, get_db
from sqlalchemy.orm import Session
from app import crud
from app.schemas import Movie, Suggestion
from app.logger import logger

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Suggestion API", docs_url="/swagger")


@app.post("/suggestions/genre", response_model=Suggestion)
def get_suggestions_genre(user_id: int, db: Session = Depends(get_db)):
    """Endpoint to suggest movies based on user preferences."""
    try:
        user_preferences = crud.get_user_preferences(user_id)
        if not user_preferences:
            logger.error("Error en ejecucion")
            raise HTTPException(status_code=404, detail="User preferences not found")

        genres = [pref.genre for pref in user_preferences]
        # Example: Return top 3 movies for each preferred genre
        suggestions = []
        for genre in genres:
            suggestions.extend(crud.get_movies_by_genre(db, genre)[:3])

        logger.info("Exito en ejecucion")
        return {"user_id": user_id, "suggestions": suggestions}
    except Exception as e:
        logger.error("Error en ejecucion")
        raise HTTPException(status_code=500, detail="Internal Server Error") from e
