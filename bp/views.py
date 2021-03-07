from django.shortcuts import render
from . import models , forms
from django.http import HttpResponse
from django.views import generic

# Create your views here.
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

def teachers_videos(request):
    videos = models.Videos.objects.all()
    context ={'videos' : videos}
    return render (request , 'bp/teachers_videos.html' , context)

def teachers_videos_upload (request):
    form = forms.Teachers_videos_upload
    if request.method == 'POST':
        form = forms.Teachers_videos_upload(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse ("Your video uploaded successfully!")
        else:
            return HttpResponse("please try again!")
    context ={'form' : form}
    return render (request , 'bp/teachers_videos_upload.html' , context)

def teachers_videos_seen (reauest , videoid):
    return render(reauest, 'bp/teachers_videos_seen.html',{'video':models.Videos.objects.get(id=videoid)})

class students(generic.TemplateView):
    template_name='bp/students.html'

def students_exercise(request):
    exercise = models.Exercise.objects.all()
    context ={'exercise' : exercise}
    return render (request , 'bp/students_exercis.html' , context)

def students_videos(request):
    videos = models.Videos.objects.all()
    context ={'videos' : videos}
    return render (request , 'bp/students_videos.html' , context)

def student_exercise_upload (request):
    form = forms.Student_exercise_upload
    if request.method == 'POST':
        form = forms.Student_exercise_upload(request.POST , request.FILES)
        if form.is_valid ():
            form.save()
            return HttpResponse ("Your exercise uploaded successfully!")
        else:
            return HttpResponse("please try again!")
    context ={'form' : form}
    return render (request , 'bp/teachers_exercise_upload.html' , context)











def student_exercise_upload (request):
    form = forms.Student_exercise_upload
    if request.method == 'POST':
        form = forms.Student_exercise_upload(request.POST , request.FILES)
        if form.is_valid ():
            form.save()
            return HttpResponse ("OK")

    contex ={'form' : form}


    return render (request , 'bp/teachers_exercise_upload.html' , contex)






def teachers_videos_upload (request):
    form = forms.Teachers_videos_upload
    if request.method == 'POST':
        form = forms.Teachers_videos_upload(request.POST , request.FILES)
        if form.is_valid ():
            form.save()
            return HttpResponse ("OK")

    contex ={'form' : form}


    return render (request , 'bp/teachers_videos_upload.html' , contex)


def teachers_videos_seen (reauest , videoid):
    return render(reauest, 'bp/teachers_videos_seen.html',{'video':models.Videos.objects.get(id=videoid)})
