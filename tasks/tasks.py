from datetime import datetime, timezone, timedelta

from tracking_tasks_project.celery import app
from .models import Task
from .telegram_utils import send_telegram_message


@app.task
def deadline_check():
    now = datetime.now(timezone.utc)
    for task in Task.objects.all():
        minutes_left = int((task.deadline - now).total_seconds() // 60)
        minutes_after = int((now - task.deadline).total_seconds() // 60)
        if timedelta(seconds=1) < task.deadline - now <= timedelta(minutes=10):
            message = f"⚠️ Задаче '{task.title}' с ID {task.id} осталось {minutes_left} минут(ы)!"
            send_telegram_message(task.telegram_user_id, message)
        elif (task.deadline - now).total_seconds() < 0:
            message = f"⚠️ Задача '{task.title}' с ID {task.id} просрочена на {minutes_after} минут(ы"
            send_telegram_message(task.telegram_user_id, message)
