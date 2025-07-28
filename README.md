# RunningService

## 🧱 Архитектура проекта

```
.
├── backend/ # FastAPI
│ ├── main.py # точка входа
│ ├── models.py # модели БД (SQLAlchemy)
│ ├── schemas.py # Pydantic-схемы
│ ├── database.py # подключение к БД
│ └── api/ # роуты (например, /runs)
│
├── frontend/ # Vue.js (создан через Vue CLI или Vite)
│ ├── src/
│ │ ├── views/ # страницы
│ │ ├── components/ # компоненты (график, форма)
│ │ ├── services/ # API-клиент
│ │ └── App.vue, main.js
│
├── docker-compose.yml # для stage и prod (разные параметры)
├── .env.stage, .env.prod # переменные окружения
└── README.md # инструкция по запуску
```
для Dockerfile
sudo apt update
sudo apt install python3-dev libpq-dev postgresql postgresql-contrib # для успешной установки pip install psycopg2 (уже есть в requirements)
