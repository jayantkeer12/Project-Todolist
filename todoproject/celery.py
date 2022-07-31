from __future__ import absolute_import, unicode_literals 
from celery import Celery
import os
from django.conf import settings
from pytz import timezone
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')

app = Celery('todoproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.conf.enable_utc=False
app.conf.update(timezone='Asia/kolkata')
app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
app.conf.beat_schedule={
    
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
