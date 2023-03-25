from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    user_name: str
    user_email: str
    user_password: str
    user_telephone: str

class DataUserSchema(BaseModel):
    user_name: str
    user_password: str
