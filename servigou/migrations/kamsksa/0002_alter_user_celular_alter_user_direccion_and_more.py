# Generated by Django 4.1.2 on 2022-11-18 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servigou', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='celular',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='direccion',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='documento',
            field=models.IntegerField(null=True),
        ),
    ]