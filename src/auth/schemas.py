from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    role_id: int
    username: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class ConfigDict:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    role_id: int
    username: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass