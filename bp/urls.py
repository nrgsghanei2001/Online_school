from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static
app_name='bp'

urlpatterns = [
    path ('' , views.home.as_view() , name ="home"),
    path('teachers/', views.teachers.as_view() ,name='teachers'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
