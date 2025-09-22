# import os
# from celery import Celery
# os.environ.setdefault("DJANGO_SETTINGS_MODULE","tutoring_api.settings")

# app =  Celery("tutoring_api")
# app.config_from_object("django.conf:settings", namespace = "CELERY")
# app.autodiscover_tasks()


import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutoring_api.settings")

app = Celery("tutoring_api")
app.config_from_object("django.cof:settings", namespace= "CELERY")
app.autodiscover_tasks()