from django.contrib import admin
from . import models
from .models import Videos

@admin.register(models.exercises)
class ExercisesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Videos)
