from pydantic import BaseModel, Field,EmailStr

class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(gt=0, lt=120)

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int

    model_config = {"from_attributes": True}