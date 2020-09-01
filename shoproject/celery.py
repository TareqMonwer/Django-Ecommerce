import os
from celery import Celery


# Set the default Django settings for the celery app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoproject.settings')

app = Celery('shoproject')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()