from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static
app_name='bp'

urlpatterns = [
    path ('' , views.home.as_view() , name ="home"),
    path('teachers/', views.teachers.as_view() ,name='teachers'),
    path ('teachers/exercise' , views.teachers_exercise, name ="teachers_exercise"),
    path('teachers/exercise/upload' , views.teachers_exercise_upload,name="teachers_exercise_upload"),
    path('teachers/exercise/answers/<int:answer_id>' , views.teachers_exercise_answers , name="teachers_exercise_answers"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
