import datetime
from typing import Optional

from fastapi_users import schemas
from fastapi_users import models
from pydantic import EmailStr


class BaseUser(schemas.BaseModel):
    id: models.ID
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]

    class Config:
        orm_mode = True


class UserRead(BaseUser):
    other_name: Optional[str]
    phone: Optional[str]
    birthday: Optional[datetime.date]
    is_superuser: Optional[bool]


class UserUpdate(schemas.CreateUpdateDictModel, UserRead):
    pass


class AdminUpdate(UserUpdate):
    id: models.ID
    city: Optional[int]
    additional_info: Optional[str]
    is_active: Optional[bool]
    is_verified: Optional[bool]


class AdminRead(schemas.BaseUser[int], AdminUpdate):
    id: models.ID


class UserCreate(schemas.BaseUserCreate, AdminUpdate):
    first_name: str
    last_name: str
    email: EmailStr
    is_superuser: bool
    password: str
