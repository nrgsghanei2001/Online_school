from django.conf.urls import url
from . import views
app_name='bp'

urlpatterns = [
    url(r'^$',views.Index.as_view(),name='index'),
    url(r'^students/$',views.studentslistView.as_view(),name='students'),
    url('upload/$',views.exerciseUpload.as_view(),name='upload'),
    url('login/$',views.login.as_view(),name='login'),
]
