import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracking_tasks_project.settings')

app = Celery('tracking_tasks_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'deadline-check-every-minute': {
        'task': 'tasks.tasks.deadline_check',
        'schedule': crontab(minute='*/1'),
    },
}
