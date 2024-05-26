from pydantic import BaseModel, Field
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]  # Ushbu qatorga `Optional` va `bool` ni qo'shing

    class Config:
        schema_extra = {
            "example": {
                'username': "diordev",
                'email': 'diordev@gmail.com',
                'password': 'diordev2004',
                'is_staff': False,
                'is_active': True
            }
        }
