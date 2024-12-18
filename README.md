# Mountain Pass API

## Описание
Это проект для управления информацией о горных перевалах. Он включает создание, добавление и модерацию записей о перевалах через REST API. Этот проект использует **FastAPI** для создания API и **PostgreSQL** для хранения данных.

## Требования

- Python 3.8 или выше
- PostgreSQL
- Библиотеки Python, указанные в `requirements.txt`

## Установка

1. Клонируйте репозиторий:


   git clone https://github.com/PanDo4ka79/spr
   cd spr

2. Создайте виртуальное окружение:

python3 -m venv venv

3. Активируйте виртуальное окружение:

venv\Scripts\activate

4. Установите зависимости:

pip install -r requirements.txt

5. Убедитесь, что база данных PostgreSQL запущена и доступна.

6. Запустите сервер FastAPI:

uvicorn main:app --reload
После этого сервер будет доступен по адресу http://127.0.0.1:8000

## Как использовать API
Добавление нового перевала
POST /submitData

Запрос:

{
  "name": "Pass Name",
  "description": "Description of the mountain pass."
}

Ответ:

{
  "id": 1,
  "name": "Pass Name",
  "description": "Description of the mountain pass.",
  "status": "new"
}

## Получение всех перевалов
GET /passes 

Ответ:

[
  {
    "id": 1,
    "name": "Pass Name",
    "description": "Description of the mountain pass.",
    "status": "new",
    "created_at": "2024-12-18T00:00:00"
  }
]
## Тестирование

1. Запустите сервер с помощью команды:

uvicorn main:app --reload

2. Откройте Swagger UI для тестирования API.
