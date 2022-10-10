from dataclasses import dataclass
from dataclasses_json import dataclass_json
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# TODO: Extend 'User' to create relationship to the actual business logic
#       of the application.
#
#       E.g. what can the user create/modify/delete in this application

@dataclass_json
@dataclass
class User(UserMixin):
    id: str
    username: str
    email: str
    hashed_password: str

    def __repr__(self) -> str:
        return f'User {self.username} [{self.email}]'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.hashed_password, password)
