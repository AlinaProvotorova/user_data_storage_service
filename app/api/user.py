from itertools import zip_longest
from typing import Dict, List, Union

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import (auth_backend, current_superuser,
                           current_user, fastapi_users)
from app.crud.user_crud import get_all_users_from_db
from app.schemas.user import (AdminRead, AdminUpdate, BaseUser,
                              UserCreate, UserRead, UserUpdate)

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    tags=['auth'],
)

users_router = fastapi_users.get_users_router(UserRead, UserUpdate)
users_router.routes = [
    rout for rout in users_router.routes if 'current' in rout.name
]
router.include_router(
    users_router,
    prefix="/users/current",
    tags=["user"]
)

admin_router = fastapi_users.get_users_router(AdminRead, AdminUpdate)
admin_router.routes = [
    rout for rout in admin_router.routes if 'current' not in rout.name
]
router.include_router(
    admin_router,
    prefix="/private/users",
    tags=["admin"],
    dependencies=[Depends(current_superuser)]
)

router.include_router(
    fastapi_users.get_register_router(AdminRead, UserCreate),
    prefix='/private/users',
    tags=['admin'],
    dependencies=[Depends(current_superuser)]
)


@router.get(
    '/users/current',
    response_model=Dict[str, Union[List[BaseUser], Dict]],
    response_model_exclude_none=True,
    dependencies=[Depends(current_user)],
    tags=['admin', 'user'],
)
async def get_all_users(
        size: int = 0,
        page: int = 1,
        session: AsyncSession = Depends(get_async_session),
):
    """Постраничное получение кратких данных обо всех пользователях"""
    all_users = await get_all_users_from_db(session)
    if size > len(all_users):
        raise HTTPException(
            status_code=400,
            detail="Максимальный размер превышает количество пользователей,"
                   f" максимальное количество = {len(all_users)},"
                   " или введите 0 для вывода всех пользователей",
        )
    if size != 0:
        user = iter(all_users)
        pages = list(zip_longest(
            *[user for i in range(size)]
        ))
    else:
        pages = (all_users,)
        size = len(pages)
    try:
        data = pages[page - 1]
    except IndexError:
        raise HTTPException(
            status_code=400,
            detail="Такой страницы не существует "
                   f"максимальный номер старицы = {len(pages)}",
        )
    return dict(
        data=data,
        meta=dict(
            pagination=dict(
                total=len(pages),
                page=page,
                size=len(pages) if size == 0 else size
            )
        )
    )
