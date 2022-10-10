from app.models import User


users = [
    {
        "id": "1",
        "username": "testuser",
        "email": "test@user.com",
        "hashed_password": "pbkdf2:sha256:260000$zXt0trr65eSmRLKj$5f0c713a2eb0eeaff59902af2849b1f25fb097332578636eba32d294da9c4672"  # noqa E502
    }
]


class MemRepo:
    _data = []

    def __init__(self) -> None:
        self._data = users

    def get_user(self, username: str) -> User:
        for user in self._data:
            if user["username"] == username:
                return User.from_dict(user)

        return None

    def get_user_by_id(self, id: int) -> User:
        for dev in self._data:
            if dev["id"] == id:
                return User.from_dict(dev)

        return None

    def get_user_by_email(self, email: str) -> User:
        for user in self._data:
            if user["email"] == email:
                return User.from_dict(user)

        return None

    def get_id(self) -> str:
        return str(len(self._data) + 1)

    def add(self, user: User):
        self._data.append(user.to_dict())
