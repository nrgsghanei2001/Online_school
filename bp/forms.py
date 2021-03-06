from django import forms
from django.forms import ModelForm
from .models import Videos

class CreateVideo(ModelForm):
    class Meta:
        model = Videos
        fields= '__all__'
