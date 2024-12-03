from sqlalchemy import Column, Integer, String, Date
from app.database import Base


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String, index=True)

    # New columns
    director = Column(String, index=True)
    writer = Column(String, index=True)
    studio = Column(String, index=True)
    running_time = Column(Integer)  # Assuming running time in minutes
    language = Column(String, index=True)
    release_date = Column(Date)  # Using Date type for dates
