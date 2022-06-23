from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload, name='upload'),
    path('category/<slug:cat_slug>/', select_cat, name='select-cat'),
    path('file/<slug:file_slug>/', select_file, name='select-file'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logoutuser, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('about/', about, name='about'),
    path('addWork/', add_work, name='add-work'),
]