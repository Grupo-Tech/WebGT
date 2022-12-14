# Generated by Django 3.0 on 2019-12-07 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191206_1451'),
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
        migrations.CreateModel(
            name='Carrucel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=90, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=110, verbose_name='Descripcion')),
                ('imagenes', models.ImageField(upload_to='', verbose_name='Imagenes')),
                ('estado', models.BooleanField(default=True, verbose_name='Carrusel Activo/ Autor Inactivo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Categoria')),
            ],
            options={
                'verbose_name': 'Carrucel',
                'verbose_name_plural': 'Carruceles',
            },
        ),
    ]
