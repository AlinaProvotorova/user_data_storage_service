from typing import Optional
from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Cервис для хранения данных о пользователях'
    database_url: str = 'sqlite+aiosqlite:///./userService.db'
    secret: str = 'secret'
    superuser_email: Optional[EmailStr] = None
    superuser_password: Optional[str] = None
    superuser_first_name: Optional[str] = None
    superuser_last_name: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
