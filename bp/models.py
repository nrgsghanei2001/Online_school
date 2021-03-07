from django.db import models
from datetime import datetime

class Exercise(models.Model):
    name=     models.CharField(max_length=200)
    file =    models.FileField( upload_to="exercise")
    deadline= models.DateTimeField( auto_now=False, auto_now_add=False ,null=True,blank=True)


class Answers(models.Model):
    exercise=  models.ForeignKey("Exercise", on_delete=models.CASCADE, null=True)
    number=    models.IntegerField()
    file =     models.FileField( upload_to="exercise")
    deadline=  models.DateTimeField(default=datetime.now(), blank=True)
    score=     models.IntegerField(default=100)

    def __str__ (self):
        return str(self.number)


class Videos(models.Model):
    name= models.CharField( max_length=300,null=True)
    file= models.FileField( upload_to="videos" , null=True)

    def __str__ (self):
        return self.name
