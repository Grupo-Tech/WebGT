# Generated by Django 3.0 on 2019-12-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191207_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrucel',
            name='imagenes',
            field=models.ImageField(upload_to='Agregar', verbose_name='Imagenes'),
        ),
    ]
