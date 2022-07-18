from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView, DetailView
from django.contrib import messages
from django.utils import timezone

from cart import cart
from cart.cart import Cart
from cart.forms import CartAddProductForm
from .forms import *
from .models import *
from .utils import *
# biletskyi_labhunter

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


#def upload(request):
#    context = {}
#    if request.method == "POST":
#        uploaded_file = request.FILES['document']
#        fs = FileSystemStorage()
#        name = fs.save(uploaded_file.name, uploaded_file)
#        context['url'] = fs.url(name)
#    return render(request, 'service/upload.html', context)



class ServiceHome(DataMixin, ListView):
    model = Files
    template_name = 'service/home.html'
    context_object_name = 'files'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Головна сторінка')
        return dict(list(context.items()) + list(c_def.items()))


#def home(request):
#    files = Files.objects.all()
#    categories = Category.objects.all()
#
#    context = {
#        'files': files,
#        'menu': menu,
#        'categories': categories,
#        'cat_selected': 0,
#        'title': 'Головна сторінка',
#    }
#    return render(request, 'service/home.html', context=context)
#class ShowFile(DataMixin, DetailView):
#    model = Files
#    template_name = 'service/file.html'
#    slug_url_kwarg = 'file_slug'
#    context_object_name = 'file'
#
#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        c_def = self.get_user_context(title='categories')
#        return dict(list(context.items()) + list(c_def.items()))

def about(request):
    return HttpResponse('Про сайт')

class ShowCat(DataMixin, ListView):
    model = Files
    template_name = 'service/home.html'
    context_object_name = 'files'
    allow_empty = False
    def get_queryset(self):
        return Files.objects.filter(cat__cat_slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категорія - ' + str(context['files'][0].cat), cat_selected=str(context['files'][0].cat))
        return dict(list(context.items()) + list(c_def.items()))

#def select_cat(request, cat_slug):
#    files = Files.objects.filter(cat__cat_slug=cat_slug)
#    categories = Category.objects.all()
#
#    if len(files) == 0:
#        raise Http404()
#
#    context = {
#        'files': files,
#        'categories': categories,
#        'menu': menu,
#        'title': 'Вибір по рубрикам',
#        'cat_selected': cat_slug,
#    }
#    return render(request, 'service/home.html', context=context)


def select_file(request, file_slug):
    file = get_object_or_404(Files, file_slug=file_slug)
    categories = Category.objects.all()
    cart_file_form = CartAddProductForm()
    login_menu = menu.copy()
    shop_cart = cart.Cart(request)
    all_file = set()
    for fd in Files.objects.all():
        all_file.add(fd.id)
    for sc in shop_cart:
        if sc['file'].id in all_file:
            all_file.remove(sc['file'].id)
        else:
            pass
    if not request.user.is_authenticated:
        login_menu.pop(1)
    context = {
        'file': file,
        'menu': login_menu,
        'title': file.title,
        'categories': categories,
        'cat_selected': file.cat_id,
        'cart_file_form': cart_file_form,
        'shop_cart': shop_cart,
        'all_file': all_file,
    }

    return render(request, 'service/file.html', context=context)


def contact(request):
    return HttpResponse("Зворотній зв'язок")


#def login(request):
#    if request.method == 'POST':
#        form = Test(request.POST)
#        if form.is_valid():
#            print((form.cleaned_data.get('title') == "Міша"))
#    else:
#        form = Test()
#    return render(request, 'service/login.html', {'form': form})


class AddWork(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddFileForm
    template_name = 'service/upload.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Завантаження роботи')
        return dict(list(context.items()) + list(c_def.items()))

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

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'service/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизація')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logoutuser(request):
    logout(request)
    return redirect('login')


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         file=item['file'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'service/created.html',
                          {'order': order, 'title': 'Thank you', })
    else:
        form = OrderCreateForm
    return render(request, 'service/create.html',
                  {'cart': cart, 'form': form, 'title': 'Checkout', })
