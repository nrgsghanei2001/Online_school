from django.shortcuts import render
from . import models , forms
from django.http import HttpResponse
from django.views import generic

class home (generic.TemplateView):
    template_name='bp/home.html'

class teachers (generic.TemplateView):
    template_name= 'bp/teachers.html'

def teachers_exercise(request):
    exercise = models.Exercise.objects.all()
    context ={'exercise' : exercise}
    return render (request , 'bp/teachers_exercis.html' , context)

def teachers_exercise_upload (request):
    form = forms.Teachers_exercise_upload
    if request.method == 'POST':
        form = forms.Teachers_exercise_upload(request.POST , request.FILES)
        if form.is_valid ():
            form.save()
            return HttpResponse ("Your exercise uploaded successfully!")
        else:
            return HttpResponse("please try again!")
    context ={'form' : form}
    return render (request , 'bp/teachers_exercise_upload.html' , context)

def teachers_exercise_answers (request,answer_id):
    answers=models.Answers.objects.filter(exercise=models.Exercise.objects.get(id=answer_id))
    context={'answers':answers}
    return render (request , 'bp/teachers_exercise_answers.html' , context)
