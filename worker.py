# worker.py
from tasks.celery import celery

if __name__ == '__main__':
    # Celeryワーカーを起動
    celery.worker_main(['worker', '--pool=solo', '--loglevel=info'])
