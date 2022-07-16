from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from service.utils import menu
from .cart import Cart
from .forms import CartAddProductForm
from service.models import *


@require_POST
def cart_add(request, file_id):
    cart = Cart(request)
    file = get_object_or_404(Files, id=file_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(file=file,
                 quantity=1,
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, file_id):
    cart = Cart(request)
    file = get_object_or_404(Files, id=file_id)
    cart.remove(file)
    return redirect('cart:cart_detail')




def cart_detail(request):
    cart = Cart(request)
    categories = Category.objects.all()
    login_menu = menu.copy()
    if not request.user.is_authenticated:
        login_menu.pop(1)
    context = {
        'menu': login_menu,
        'categories': categories,
        'cart': cart,
        'title': 'Корзина',
        'previous_url': request.META.get('HTTP_REFERER'),

    }
    return render(request, 'cart/detail.html', context=context)
