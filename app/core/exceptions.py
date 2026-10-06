class UserNotFoundException(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.message = f"User with id {user_id} not found"
        super().__init__(self.message)


class DuplicateUserException(Exception):
    def __init__(self, email: str):
        self.email = email
        self.message = f"User with email {email} already exists"
        super().__init__(self.message)