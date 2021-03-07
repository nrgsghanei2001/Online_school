from django.contrib import admin
from . import models

admin.site.register(models.Videos)
admin.site.register(models.Exercise)
admin.site.register(models.Answers)
