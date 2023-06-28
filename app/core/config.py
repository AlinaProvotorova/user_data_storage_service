import logging
from typing import Optional

import uvicorn
from pydantic import BaseSettings, EmailStr
from uvicorn.logging import DefaultFormatter

log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
logger = logging.getLogger("uvicorn")
handler = logging.StreamHandler()
console_formatter = uvicorn.logging.ColourizedFormatter(
    "{levelprefix:<8} {message}",
    style="{",
    use_colors=True
)
handler.setFormatter(console_formatter)


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
