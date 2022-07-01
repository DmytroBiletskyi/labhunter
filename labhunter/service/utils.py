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
        return context