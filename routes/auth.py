from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from core.database import get_db
from schemas.users import LoginSchema, UserCreate, UserResponse
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


@auth_router.post('/login')
async def login(login_schema: LoginSchema, db: AsyncSession=Depends(get_db)):
    """
    Login endpoint.
    """
    try:
        return await AuthService.login(login_schema, db)
    except ValueError as e:
        raise HTTPException(
            status_code=400, 
            detail=str(e))


@auth_router.post('/refresh')
async def refresh(refresh_token: str):
    """
    Refresh access token endpoint.
    """
    try:
        return await AuthService.use_refresh_token(refresh_token)
    except ValueError as e:
        raise HTTPException(
            status_code=401, 
            detail=str(e))


@auth_router.get('/me', response_model=UserResponse)
async def me(token: str, db: AsyncSession=Depends(get_db)):
    """
    Get current user endpoint.
    """
    try:
        return await AuthService.get_current_user(token, db)
    except ValueError as e:
        raise HTTPException(
            status_code=401, 
            detail=str(e))
    