from fastapi import HTTPException

from core.security import verify_token
from repositories.outfit_repository import OutfitRepository

class OutfitService:

    @staticmethod
    async def create_outfit(session, outfit_schema, token):

        payload = verify_token(token, expected_type="access")

        user_id = int(payload.get("sub"))

        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token: missing subject")
        
        outfit_data = {
            **outfit_schema.model_dump(),
            "user_id": user_id
        }

        outfit = await OutfitRepository.create(session, outfit_data)

        if not outfit:
            raise HTTPException(status_code=500, detail="Failed to create outfit")
        
        return 