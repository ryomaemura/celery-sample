from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from celery import Celery
from tasks.celery import calc_bmi

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Celeryのインスタンスを作成
celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",  # Redisの接続先
    backend="redis://localhost:6379/0"  # Redisの接続先
)


@app.get("/")
async def root():
    return {"message": "Hello Celery"}


@app.get("/sampleCelery")
async def sample_celery():
    print("sample_celery 起動")
    calc_bmi.delay(1.7, 50)
    print("sample_celery 実行後")
    return {"message": "response sample_celery"}
