from django.db import models


class DataTimeMixin:
    data_created = models.DateTimeField(auto_now=True)
    data_updated = models.DateTimeField(auto_now=True)
