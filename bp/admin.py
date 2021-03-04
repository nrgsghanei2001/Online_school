from django.contrib import admin
from . import models

@admin.register(models.exercises)
class ExercisesAdmin(admin.ModelAdmin):
    name='bp/admin/exersises/upload.html'
