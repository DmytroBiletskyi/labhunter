from django.db import models
from django.urls import reverse


class Files(models.Model):
    teacher = models.CharField(max_length=255, verbose_name='Викладач')
    docx = models.FileField(upload_to='files/docx/', verbose_name='Шлях до документу')
    topic = models.CharField(max_length=255, null=True, verbose_name='Тема роботи')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='Титулка')
    work_number = models.IntegerField(null=True, blank=True, verbose_name='Номер роботи')
    other_files = models.FileField(upload_to='files/other/', blank=True, verbose_name='Дадаткові файли')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name='Категорія')
    sub = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Предмет')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Усі файли'
        verbose_name_plural = 'Усі файли'


class Category(models.Model):
    cat_name = models.CharField(max_length=100, db_index=True, verbose_name='Категорія')

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse('select-cat', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категорії'
        verbose_name_plural = 'Категорії'


class Subject(models.Model):
    sub_name = models.CharField(max_length=255, db_index=True, verbose_name='Назва предмету')
    course = models.IntegerField(verbose_name='Курс')
    semester = models.IntegerField(verbose_name='Семестр')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name = 'Предмети'
        verbose_name_plural = 'Предмети'


# from service.models import *