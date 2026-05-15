from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import DATABASE_URL

db = create_async_engine(DATABASE_URL,
                         echo=True)

SessionLocal = sessionmaker(
    expire_on_commit=False,
    class_=AsyncSession,
    bind=db)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as session:
        yield session