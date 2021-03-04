from django.conf.urls import url
from . import views
app_name='bp'

urlpatterns = [
    url(r'^$',views.Index.as_view(),name='index'),
    url(r'^exercises/$',views.ExercisesListView.as_view(),name='exercises'),
    url(r'^upload/$',views.exerciseUpload.as_view(),name='upload'),
]
