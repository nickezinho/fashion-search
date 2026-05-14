from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///./test.db")

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=db)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
