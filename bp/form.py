from django import forms
from django.forms import ModelForm
from .models import Videos

class Teachers_videos_upload(ModelForm):
    class Meta:
        model = Videos
        fields= '__all__'
