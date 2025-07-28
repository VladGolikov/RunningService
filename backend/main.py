from fastapi import FastAPI
from backend.database import Base, engine
from backend.api.runs import router as runs_router

# Создаём таблицы в БД
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Running Stats API")

# Подключаем роутер
app.include_router(runs_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Running Stats API"}