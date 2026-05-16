from models.outfits import Outfit
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class OutfitRepository:

    @staticmethod
    async def create(session: AsyncSession, outfit_data) -> Outfit:

        outfit = Outfit(**outfit_data)

        session.add(outfit)
        await session.commit()
        await session.refresh(outfit)
        return outfit