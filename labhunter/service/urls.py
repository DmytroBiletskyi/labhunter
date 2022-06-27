from django.urls import path
from .views import *

urlpatterns = [
    path('', ServiceHome.as_view(), name='home'),
    path('upload/', upload, name='upload'),
    path('category/<slug:cat_slug>/', select_cat, name='select-cat'),
    path('file/<slug:file_slug>/', select_file, name='select-file'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logoutuser, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('about/', about, name='about'),
    path('addWork/', AddWork.as_view(), name='add-work'),
]