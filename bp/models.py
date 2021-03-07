from django.db import models
from django.urls import reverse
import uuid

class studentNumber(models.Model):
    studentcode=  models.IntegerField()

class exercises(models.Model):
    caption = models.CharField(max_length=100,null=True)
    deadline= models.DateField(null=True,blank=True)

    def __str__(self):
        return self.caption

class Date(models.Model):
    dateofSend=   models.DateField(null=True,blank=True)

class score(models.Model):
    scores=       models.IntegerField()

class Videos(models.Model):
    caption = models.CharField(max_length=100,null=True)
    Vids=     models.FileField(upload_to='videos/upload/')

    def __str__(self):
        return self.caption
