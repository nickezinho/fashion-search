from sqlalchemy import Column, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, index=True)
    username = Column("username", String, unique=True, index=True)
    email = Column("email", String, unique=True, index=True)
    hashed_password = Column("hashed_password", String)