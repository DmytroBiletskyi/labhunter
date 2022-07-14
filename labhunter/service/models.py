from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy


class Files(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва файлу')
    teacher = models.CharField(max_length=255, verbose_name='Викладач')
    docx = models.FileField(upload_to='files/docx/', verbose_name='Шлях до документу')
    topic = models.CharField(max_length=255, null=True, verbose_name='Тема роботи')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='Титулка')
    work_number = models.IntegerField(null=True, blank=True, verbose_name='Номер роботи')
    other_files = models.FileField(upload_to='files/other/', blank=True, verbose_name='Дадаткові файли')
    file_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    google_docx = models.URLField(max_length=200, null=True, unique=True, blank=True, verbose_name='Посилання на файл')
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name='Ціна')
    discount_price = models.FloatField(blank=True, null=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категорія')
    sub = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Предмет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('select-file', kwargs={'file_slug': self.file_slug})
#
   # def get_add_to_cart_url(self):
   #     return reverse("service:add-to-cart", kwargs={
   #         "pk": self.pk
   #     })
#
   # def get_remove_from_cart_url(self):
   #     return reverse("service:remove-from-cart", kwargs={
   #         "pk": self.pk
   #     })

    class Meta:
        verbose_name = 'Усі файли'
        verbose_name_plural = 'Усі файли'


class Category(models.Model):
    cat_name = models.CharField(max_length=100, db_index=True, verbose_name='Категорія')
    cat_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse('select-cat', kwargs={'cat_slug': self.cat_slug})

    class Meta:
        verbose_name = 'Категорії'
        verbose_name_plural = 'Категорії'


class Subject(models.Model):
    sub_name = models.CharField(max_length=255, db_index=True, verbose_name='Назва предмету')
    course = models.IntegerField(verbose_name='Курс')
    semester = models.IntegerField(verbose_name='Семестр')
    sub_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name = 'Предмети'
        verbose_name_plural = 'Предмети'


#class OrderItem(models.Model):
#    user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                             on_delete=models.CASCADE)
#    ordered = models.BooleanField(default=False)
#    item = models.ForeignKey('Files', on_delete=models.CASCADE)
#    quantity = models.IntegerField(default=1)
#
#    def __str__(self):
#        return f"{self.quantity} of {self.item.title}"
#
#
#class Order(models.Model):
#    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    items = models.ManyToManyField(OrderItem)
#    start_date = models.DateTimeField(auto_now_add=True)
#    ordered_date = models.DateTimeField()
#    ordered = models.BooleanField(default=False)
#
#    def __str__(self):
#        return self.user.username
#
## from service.models import *
#