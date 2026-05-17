from models.outfits import Outfit
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import json

class OutfitRepository:

    @staticmethod
    async def create(session: AsyncSession, outfit_data) -> Outfit:


        if outfit_data.get("embedding"):
            outfit_data["embedding"] = json.dumps(
                outfit_data["embedding"]
            )

        outfit = Outfit(**outfit_data)

        session.add(outfit)
        await session.commit()
        await session.refresh(outfit)
        return outfit
    
