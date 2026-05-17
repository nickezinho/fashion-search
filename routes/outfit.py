from fastapi import APIRouter, Depends, HTTPException
from core.database import get_db
from core.security import verify_token
from sqlalchemy.ext.asyncio import AsyncSession
from models.outfits import Outfit
from services.outfit_service import OutfitService
from schemas.outfits import OutfitCreate
from sqlalchemy import select

outfit_router = APIRouter(prefix='/outfits', tags=['Outfits'], dependencies=[Depends(verify_token)])

@outfit_router.get('/')
async def get_outfits(session: AsyncSession=Depends(get_db)):
    """
    Get all outfits endpoint.
    """
    result = await session.execute(select(Outfit))

    outfits = result.scalars().all()
    return {
        'testar': 'endpoint de outfits',
        'outfits': outfits
    }

@outfit_router.post('/create')
async def create_outfit(outfit: OutfitCreate, token: str, session: AsyncSession=Depends(get_db)):
    """
    Create a new outfit endpoint.
    """
    try: 
        outfit = await OutfitService.create_outfit(session, outfit, token)
        return {
            'message': 'Outfit created successfully',
            'outfit': outfit
        }
    
    except ValueError as e:
        raise HTTPException(
            status_code=400, 
            detail=str(e))