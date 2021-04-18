from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.sign_up, name='sign_up'), 
    path('SignIn',views.sign_in, name='sign_in'), 
    path('files',views.files_list,name='files_list'),
    path('files/upload',views.file_upload,name='file_upload'),
    path('home',views.home,name='home')
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)