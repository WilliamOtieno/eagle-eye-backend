import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EagleEye.settings")

app = Celery("EagleEye")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(
    task_track_started=True,
    worker_send_task_events=True,
    task_send_sent_event=True,
    result_expires=3600*24*30,
    task_acks_late=True,
    task_reject_on_worker_lost=True,
)
app.autodiscover_tasks()
