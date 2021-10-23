# Generated by Django 3.2.6 on 2021-10-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210928_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_special',
            field=models.BooleanField(default=False, verbose_name='عضویت ویژه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویش'), ('p', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]