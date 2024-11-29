def suggest_movies(preferences):
    """Simple algorithm to suggest movies based on user preferences."""
    genres = [pref.genre for pref in preferences]
    # Example: Return top 3 movies for each preferred genre
    suggestions = []
    for genre in genres:
        suggestions.extend(crud.get_movies_by_genre(db, genre)[:3])
    return suggestions