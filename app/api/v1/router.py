from fastapi import APIRouter, Depends
from app.api.dependencies import get_user_service
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

api_router = APIRouter()

@api_router.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@api_router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user_by_id(user_id)

