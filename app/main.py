from fastapi import FastAPI

from app.api.user import router
from app.core.config import settings, log_config, logger
from app.core.init_db import create_first_superuser

app = FastAPI(title=settings.app_title)

app.include_router(router)


@app.on_event('startup')
async def startup():
    await create_first_superuser()


logger.info('Документация доступна по адресу: http://127.0.0.1:5000/docs')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'main:app',
        reload=True,
        log_config=log_config
    )
