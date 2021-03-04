from django.db import models
from django.urls import reverse
import uuid

class studentNumber(models.Model):
    studentcode=  models.IntegerField()

class exercises(models.Model):
    pass

class Date(models.Model):
    dateofSend=   models.DateField(null=True,blank=True)

class score(models.Model):
    scores=       models.IntegerField()
