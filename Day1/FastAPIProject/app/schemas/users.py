from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserRequest(BaseModel):
    username: str
    age: int
    gender: Gender

