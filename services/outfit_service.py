from repositories.outfit_repository import OutfitRepository

class OutfitService:

    @staticmethod
    async def create_outfit(session, outfit_schema, user_id):

        outfit_data = {
            **outfit_schema.model_dump(),
            "user_id": user_id
        }

        return await OutfitRepository.create(session, outfit_data)