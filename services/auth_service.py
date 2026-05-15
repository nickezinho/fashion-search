from repositories.user_repository import UserRepository
from core.security import hash_password

class AuthService:

    @staticmethod
    async def register_user(session, user_schema):
        
        newUserschema = user_schema.model_copy()

        newUserschema.password = hash_password(newUserschema.password)

        existing_user = await UserRepository.get_email(session, user_schema.email)
        if existing_user:
            raise ValueError('Email already registered')

        new_user = await UserRepository.create(session, newUserschema)
        return {
            "message": "User registered successfully",
            "user": new_user
        }

       