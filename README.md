# user_data_storage_service

Cервис для хранения данных о пользователях.
Сервис выполнен с помощью фреймворка FastApi Users.

## Запуск приложения:

- Клонируйте репозиторий командой в терминале:

```commandline
...$  git clone https://github.com/AlinaProvotorova/user_data_storage_service.git
```

- В репозитории создайте файл ```.env```, где необходимо прописать данные переменные окружения:

```commandline
SECRET='secret'            #секретный ключ
SUPERUSER_EMAIL="..."      #email для суперпользователя
SUPERUSER_PASSWORD="..."   #пароль для суперпользователя
SUPERUSER_FIRST_NAME="..." #имя суперпользователя
SUPERUSER_LAST_NAME="..."  #фамилия суперпользователя
DATABASE_URL=sqlite+aiosqlite:///./the_app.db
```

- Активируйте виртуальное окружение командой:

```commandline
...$ python -m virtualenv venv && .\venv\Scripts\activate
```

- Установите зависимости командой:

```
(venv) ...$ pip install -r requirements.txt
```

```
(venv) ...$ python3 -m pip install --upgrade pip
```

- Примените миграции:

```
(venv) ...$ alembic upgrade head
```

- Запустите сервер:

```
(venv) ...$ uvicorn app.main:app --reload
```

- После запуска перейдите по [ссылке документации Swagger](http://127.0.0.1:8000/docs)


## Техно-стек:

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- Asyncio
- 
Автор: [Провоторова Алина Игоревна](https://t.me/alinamalina998)
