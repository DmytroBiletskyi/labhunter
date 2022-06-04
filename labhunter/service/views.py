from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.files.storage import FileSystemStorage

from .forms import *
from .models import *


menu = [
    {'title': "Про сайт", 'url_name': 'about'},
    {'title': "Завантажити роботу", 'url_name': 'add_work'},
    {'title': "Зворотній зв'язок", 'url_name': 'contact'},
        ]
#categories = [
#    {'title': "Лабораторні", 'url_name': 'lab'},
#    {'title': "Курсові", 'url_name': 'curs'},
#    {'title': "ДЗ", 'url_name': 'dz'},
#    {'title': "РГР", 'url_name': 'rgr'},
#]


def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'service/upload.html', context)


def home(request):
    files = Files.objects.all()
    categories = Category.objects.all()

    context = {
        'files': files,
        'menu': menu,
        'categories': categories,
        'cat_selected': 0,
    }
    return render(request, 'service/home.html', context=context)


def about(request):
    return HttpResponse("Про сайт")


def select_cat(request, cat_id):
    lab = Files.objects.filter(cat_id=cat_id)
    categories = Category.objects.all()

    context = {
        'lab': lab,
        'categories': categories,
        'menu': menu,
        'cat_selected': cat_id,
    }

    return render(request, 'service/home.html', context=context)


def contact(request):
    return HttpResponse("Зворотній зв'язок")


def login(request):
    if request.method == 'POST':
        form = Test(request.POST)
        if form.is_valid():
            print((form.cleaned_data.get('title') == "Міша"))
    else:
        form = Test()
    return render(request, 'service/login.html', {'form': form})


def register(request):
    return HttpResponse("Зареєструватись")


def add_work(request):
    return HttpResponse("Додається робота")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
