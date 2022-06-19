
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *
from .utils import *


#menu = [
#    {'title': "Про сайт", 'url_name': 'about'},
#    {'title': "Завантажити роботу", 'url_name': 'add-work'},
#    {'title': "Зворотній зв'язок", 'url_name': 'contact'},
#        ]
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
        'title': 'Головна сторінка',
    }
    return render(request, 'service/home.html', context=context)


def about(request):
    return HttpResponse("Про сайт")


def select_cat(request, cat_slug):
    files = Files.objects.filter(cat__cat_slug=cat_slug)
    categories = Category.objects.all()

    if len(files) == 0:
        raise Http404()

    context = {
        'files': files,
        'categories': categories,
        'menu': menu,
        'title': 'Вибір по рубрикам',
        'cat_selected': cat_slug,
    }
    return render(request, 'service/home.html', context=context)


def select_file(request, file_slug):
    file = get_object_or_404(Files, file_slug=file_slug)

    context = {
        'file': file,
        'menu': menu,
        'title': file.title,
        'cat_selected': file.cat_id,
    }

    return render(request, 'service/file.html', context=context)


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


def add_work(request):
    return HttpResponse("Додається робота")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'service/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Реєстрація')
        return dict(list(context.items()) + list(c_def.items()))

