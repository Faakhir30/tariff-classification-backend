# app/session/db.py

from sqlmodel import SQLModel, create_engine, Session
import os

# Database URL - replace it with your own settings
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/mydatabase")

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Dependency to get the session for the request
def get_session():
    with Session(engine) as session:
        yield session
