# tasks/celery.py
from celery import Celery
import time

# Celeryアプリケーションを作成
celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)


@celery.task(name="calc_bmi")
def calc_bmi(height, weight):
    print("create_task 起動")
    bmi = weight / (height ** 2)
    time.sleep(5)
    print(f"bmi:{bmi}")
    print("create_task 実行後")
    return True
