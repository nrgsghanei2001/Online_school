from django.contrib import admin
from . import models

class studentInline(admin.TabularInline):
    model=models.student
    extra=1
