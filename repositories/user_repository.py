from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.users import User  


class UserRepository:

    @staticmethod
    async def get_email(session: AsyncSession, email: str) -> User | None:

        result = await session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()
    
    @staticmethod
    async def create(session: AsyncSession, user_schema) -> User:

        new_user = User(
            username=user_schema.username,
            name=user_schema.name,
            email=user_schema.email,
            hashed_password=user_schema.password
            )
        
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user
