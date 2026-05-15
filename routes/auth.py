from fastapi import APIRouter, Depends, HTTPException

from core.database import get_db
from schemas.users import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

from services.auth_service import AuthService

auth_router = APIRouter(prefix='/auth', tags=['Auth'])

@auth_router.get('/')
async def home():
    """
    Login endpoint.
    """
    return {'message': 'Login endpoint'}

@auth_router.post('/register')
async def register(user: UserCreate, db: AsyncSession=Depends(get_db)):
    """
    Registration endpoint.
    """
    try:
        return await AuthService.register_user(db, user)
    except ValueError as e:
        raise HTTPException(
            status_code=400, 
            detail=str(e))

    