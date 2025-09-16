from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str


class UserInBD(User):
    hashed_password: str