from django.db import models
import uuid
class student(models.Model):
    studentcode=  models.IntegerField()
    dateofsend=   models.DateField(null=True,blank=True)
    score=        models.IntegerField()

    def get_absolute_url(self):
        return reverse('studentcodedetail',args=[str(self.id)])
    def __int__(self):
        return self.studentcode
