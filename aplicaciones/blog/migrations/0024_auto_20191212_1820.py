# Generated by Django 3.0 on 2019-12-12 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20191212_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='post',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
