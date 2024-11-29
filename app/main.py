from fastapi import FastAPI, HTTPException
from app.database import engine, Base
from app import models, crud
from app.schemas import Movie, Suggestion
from app.algorithms import suggest_movies

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Suggestion API", docs_url="/swagger")

@app.post("/suggestions", response_model=Suggestion)
def get_suggestions(user_id: int):
    """Endpoint to suggest movies based on user preferences."""
    try:
        user_preferences = crud.get_user_preferences(user_id)
        if not user_preferences:
            raise HTTPException(status_code=404, detail="User preferences not found")
        suggestions = suggest_movies(user_preferences)
        return {"user_id": user_id, "suggestions": suggestions}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e