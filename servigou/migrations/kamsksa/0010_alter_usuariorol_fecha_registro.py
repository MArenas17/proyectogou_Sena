# Generated by Django 4.1.3 on 2022-11-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servigou', '0009_alter_publicacion_user_alter_servicio_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariorol',
            name='fecha_registro',
            field=models.DateField(),
        ),
    ]