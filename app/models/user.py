from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, DateTime, String, Text, Integer
from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    other_name = Column(String)
    phone = Column(String)
    birthday = Column(DateTime)
    city = Column(Integer)
    additional_info = Column(Text)
