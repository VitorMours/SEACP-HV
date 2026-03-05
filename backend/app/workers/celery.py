from celery import Celery 

celery_app = Celery(
  __name__, 
  broker="redis://localhost:6379", 
  backend="redis://localhost:6379",
  include=["app.workers.image"]  # 👈 adiciona isso

)