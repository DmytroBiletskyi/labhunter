from decimal import Decimal
from django.conf import settings

from service.models import Files


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, file, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        file_id = str(file.id)
        if file_id not in self.cart:
            self.cart[file_id] = {'quantity': 0,
                                     'price': str(file.price)}
        if update_quantity:
            self.cart[file_id]['quantity'] = quantity
        else:
            self.cart[file_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, file):
        """
        Удаление товара из корзины.
        """
        file_id = str(file.id)
        if file_id in self.cart:
            del self.cart[file_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        file_ids = self.cart.keys()
        # получение объектов file и добавление их в корзину
        files = Files.objects.filter(id__in=file_ids)
        for file in files:
            self.cart[str(file.id)]['file'] = file

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        #print(self.cart.values())
        #for item in self.cart.values():
        #    if item['price'] == 'None':
        #        item['price'] = 2
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
