from sys import api_version
from fastapi import APIRouter, Depends
from endpoints.depends import get_user_repository
from models.users import UserIn

from repositories.users import UserRepository

router = APIRouter()

@router.get('/')
async def get_users(users: UserRepository = Depends(get_user_repository)):
    return await users.get_all()

@router.post('/create')
async def create_user(user_data: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.create(user_data=user_data)

@router.get('/get_user')
async def get_by_id(id: int, users: UserRepository = Depends(get_user_repository)):
    return await users.get_by_id(id=id)