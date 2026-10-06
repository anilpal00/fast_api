from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.core.exceptions import UserNotFoundException, DuplicateUserException

class UserService:
    def __init__(self, db:Session):
        self.repository = UserRepository(db)

    def create_user(self, user_data: UserCreate) -> User:
        existing_user = self.repository.get_user_by_email(user_data.email)
        if existing_user:
            raise DuplicateUserException(user_data.email)

        user = User(name=user_data.name, email=user_data.email, age=user_data.age)
        return self.repository.create(user)

    def get_all_users(self) -> list[User]:
        return self.repository.get_all_users()

    def get_user_by_id(self, user_id: int) -> User:
        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise UserNotFoundException(user_id)
        return user