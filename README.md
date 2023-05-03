# user_data_storage_service

Cервис для хранения данных о пользователях.
Сервис выполнен с помощью фреймворка FastApi Users.

## Чем отличается от ТЗ:

- Поле ```is_admin``` заменено на ```is_superuser```, т.к это кастомная реализация в FastApi
- Эндпоинт функций постраничного получение кратких данных обо всех пользователях одинаковый как у userа так и у админа,
  т.к. не вижу надобности дублировать, только из-за смены префикса, а данные функции выполняют абсолютно одинаковые
  действия и доступны любым зарегистрированным пользователям.

## Техно-стек:

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- Asyncio

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
```

- Активируйте виртуальное окружение командой:

```commandline
...$ python -m virtualenv venv && .\venv\Scripts\activate
```

- Установите зависимости командой:

```
(venv) ...$ python3 -m pip install --upgrade pip
```

```
(venv) ...$ pip install -r requirements.txt
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

Автор: [Провоторова Алина Игоревна](https://t.me/alinamalina998)
