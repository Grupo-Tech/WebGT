# Generated by Django 3.0 on 2019-12-10 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20191209_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='info_contactos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Direccion', models.CharField(max_length=90, verbose_name='Dirección')),
                ('Telefono', models.CharField(max_length=90, verbose_name='Teléfono')),
                ('Correo', models.EmailField(max_length=200, verbose_name='Correo Electrónico')),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('fecha_creacion', models.DateField(verbose_name='Fecha de Creacion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
