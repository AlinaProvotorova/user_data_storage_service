from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import BaseUser


async def get_all_users_from_db(
        session: AsyncSession
) -> list[BaseUser]:
    db_users = await session.execute(select(User))
    return db_users.scalars().all()
