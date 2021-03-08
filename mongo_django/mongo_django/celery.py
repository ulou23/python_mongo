from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mongo_django.settings')
app=Celery('mongo_django')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

@app.task(bind=True)
def debug(self):
    print('Req : {0!r}'.format(self.request))