# Generated by Django 4.1.3 on 2023-03-09 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servigou', '0005_rename_cantidad_dinero_servicio_celular_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='descripcion',
        ),
    ]
