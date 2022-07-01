# Generated by Django 4.0.5 on 2022-06-29 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(db_index=True, max_length=100, verbose_name='Категорія')),
                ('cat_slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорії',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(db_index=True, max_length=255, verbose_name='Назва предмету')),
                ('course', models.IntegerField(verbose_name='Курс')),
                ('semester', models.IntegerField(verbose_name='Семестр')),
                ('sub_slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Предмети',
                'verbose_name_plural': 'Предмети',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва файлу')),
                ('teacher', models.CharField(max_length=255, verbose_name='Викладач')),
                ('docx', models.FileField(upload_to='files/docx/', verbose_name='Шлях до документу')),
                ('topic', models.CharField(max_length=255, null=True, verbose_name='Тема роботи')),
                ('photo', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Титулка')),
                ('work_number', models.IntegerField(blank=True, null=True, verbose_name='Номер роботи')),
                ('other_files', models.FileField(blank=True, upload_to='files/other/', verbose_name='Дадаткові файли')),
                ('file_slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('google_docx', models.URLField(blank=True, unique=True, verbose_name='Посилання на файл')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category', verbose_name='Категорія')),
                ('sub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.subject', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Усі файли',
                'verbose_name_plural': 'Усі файли',
            },
        ),
    ]
