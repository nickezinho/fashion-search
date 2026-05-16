from datetime import timedelta

from repositories.user_repository import UserRepository
from core.security import hash_password, verify_password, create_token, verify_token


class AuthService:

    @staticmethod
    async def register_user(session, user_schema):
        
        new_user_schema = user_schema.model_copy()

        new_user_schema.password = hash_password(new_user_schema.password)

        existing_user = await UserRepository.get_email(session, user_schema.email)
        if existing_user:
            raise ValueError('Email already registered')

        new_user = await UserRepository.create(session, new_user_schema)
        return {
            "message": "User registered successfully",
            "user": new_user
        }

    @staticmethod
    async def auth_user(session, user_schema):
        
        existing_user = await UserRepository.get_username(session, user_schema.username)
        if not existing_user:
            raise ValueError('Invalid username or password')
        
        if not verify_password(user_schema.password, existing_user.hashed_password):
            raise ValueError('Invalid username or password')
        
       
        return existing_user

    @staticmethod
    async def login(login_schema, session):
        user = await AuthService.auth_user(session, login_schema)
        if not user:
            raise ValueError('Invalid username or password')
        

        access_token = create_token(user.id, token_type="access")
        refresh_token = create_token(user.id, token_type="refresh", token_duration=timedelta(days=7))

        return {
            'refresh_token': refresh_token,
            'access_token': access_token,
            'token_type': 'Bearer'
        }

    @staticmethod
    async def use_refresh_token(refresh_token):

        payload = verify_token(refresh_token, expected_type="refresh")

        user_id = int(payload.get("sub"))

        new_access_token = create_token(user_id, token_type="access")

        return {
            'access_token': new_access_token,
            'token_type': 'Bearer'
        }
        
    
    @staticmethod
    async def get_current_user(token, session):

        payload = verify_token(token, expected_type="access")

        user_id = int(payload.get("sub"))

        if not user_id:
            raise ValueError("Invalid token: missing subject")
        
        user = await UserRepository.get_id(session, user_id)

        if not user:
            raise ValueError("User not found")
        
        return user