from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload, name='upload'),
    path('category/<int:cat_id>/', select_cat, name='select-cat'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('about/', about, name='about'),
    path('addWork/', add_work, name='add_work'),
]