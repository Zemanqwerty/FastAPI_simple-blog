from typing import Optional
from pydantic import BaseModel
import datetime

class User(BaseModel):
    id_user: Optional[str] = None
    username: str
    hashed_password: str
    created_at: datetime.datetime

class UserIn(BaseModel):
    username: str
    password: str