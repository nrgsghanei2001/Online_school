from django.shortcuts import render
from django.views import generic
from . import models
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateVideo
from .models import Videos
# Imaginary function to handle an uploaded file.


class Index(generic.TemplateView):

    template_name='bp/index.html'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['students']= models.studentNumber.objects.all()
        context['date']=     models.Date.objects.all()
        context['exercise']= models.exercises.objects.all()
        context['scores']=   models.score.objects.all()
        return context

class studentslistView(generic.ListView):

    model=models.studentNumber
    template_name='bp/students_list.html'

class exerciseUpload(generic.TemplateView):

    template_name='bp/upload.html'

class login(generic.TemplateView):

    template_name='bp/login.html'

def teacherVideos(request):
    videos=Videos.objects.all()
    context={'videos':videos}
    return render(request,'bp/videos_caption.html',context)

def videoUpload(request):
    forms = CreateVideo.objects.all()
    if request.method == 'POST':
        forms = ImageForm(request.POST, request.FILES)
        forms.save()
        return HttpResponse('submision was successful')
    context={'form': form}
    return render(request, 'bp/teacher_video_upload.html', context)
#def index(request):
#    students=  models.studentNumber.objects.all()
#    date=      models.Date.objects.all()
#    exercise=  models.exercises.objects.all()
#    scores=    models.score.objects.all()

#    return render(
#        request,
#        'bp/index.html',
#        context={'students':students,'date':date,'exersise':exercise,'scores':scores}
#    )
