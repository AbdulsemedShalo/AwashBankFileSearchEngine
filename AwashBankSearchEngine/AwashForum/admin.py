from django.contrib import admin

# Import models from your Apps/models.py

from . import models

# Register your models here.
admin.site.register(models.Board)
admin.site.register(models.Post)
admin.site.register(models.Topic)
