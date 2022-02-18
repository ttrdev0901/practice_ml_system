from fastapi import APIRouter
from fastapi import Depends

from app.api.security import oauth2_schema

router = APIRouter()

@router.get('/items/')
async def read_items(token: str = Depends(oauth2_schema)):
    return {"token": token}

