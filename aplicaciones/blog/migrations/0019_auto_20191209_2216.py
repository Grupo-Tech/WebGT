# Generated by Django 3.0 on 2019-12-10 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_info_contactos_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info_contactos',
            old_name='Correo',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='info_contactos',
            old_name='Direccion',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='info_contactos',
            old_name='Telefono',
            new_name='telefono',
        ),
        migrations.AlterField(
            model_name='info_contactos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
