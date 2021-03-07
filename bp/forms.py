from django import forms
from django.forms import ModelForm
from . import models

class Teachers_exercise_upload (ModelForm):
    class Meta:
        model = models.Exercise
        fields = '__all__'
