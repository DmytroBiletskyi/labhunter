from django.db import models


class Files(models.Model):
    teacher = models.CharField(max_length=255)
    docx = models.FileField(upload_to='files/docx/')
    topic = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    work_number = models.IntegerField(null=True, blank=True)
    other_files = models.FileField(upload_to='files/other/', blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    sub = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.topic


class Category(models.Model):
    cat_name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.cat_name


class Subject(models.Model):
    sub_name = models.CharField(max_length=255, db_index=True)
    course = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return self.sub_name


# from service.models import *