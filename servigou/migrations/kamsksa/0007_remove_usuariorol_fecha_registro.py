# Generated by Django 4.1.3 on 2022-11-27 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servigou', '0006_alter_usuariorol_fecha_registro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariorol',
            name='fecha_registro',
        ),
    ]
