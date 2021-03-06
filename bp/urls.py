from django.conf.urls import url
from . import views
from django.urls import path
app_name='bp'

urlpatterns = [
    url(r'^$',views.Index.as_view(),name='index'),
    url(r'^students/$',views.studentslistView.as_view(),name='students'),
    url('upload/$',views.exerciseUpload.as_view(),name='upload'),
    url('videos/',views.teacherVideos,name='teacher_videos'),
    path('upload/', views.videoUpload, name='teacher_video_upload')
]
