import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technical_support.settings")
app = Celery("technical_support")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-paid-salary-every-2-hour-': {
        'task': 'employees.tasks.update_paid_salary',
        'schedule': crontab(minute=0, hour='*/2')
    },

}
