from django.shortcuts import render
from . import models , forms
from django.http import HttpResponse
from django.views import generic

class home (generic.TemplateView):
    template_name='bp/home.html'

class teachers (generic.TemplateView):
    template_name= 'bp/teachers.html'
