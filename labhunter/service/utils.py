from cart import cart
from .models import *

menu = [
    {'title': "Про сайт", 'url_name': 'about'},
    {'title': "Завантажити роботу", 'url_name': 'add-work'},
    {'title': "Зворотній зв'язок", 'url_name': 'contact'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        #categories = Category.objects.annotate(Count('files'))
        login_menu = menu.copy()
        if not self.request.user.is_authenticated:
            login_menu.pop(1)
        context['menu'] = login_menu
        context['categories'] = categories
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        shop_cart = cart.Cart(self.request)
        all_file = set()
        for file in Files.objects.all():
            all_file.add(file.id)
        for sc in shop_cart:
            if sc['file'].id in all_file:
                all_file.remove(sc['file'].id)
            else:
                pass
        context['all_file'] = all_file
        return context