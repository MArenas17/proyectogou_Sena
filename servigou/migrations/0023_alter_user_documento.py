# Generated by Django 4.1.3 on 2023-04-20 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servigou', '0022_alter_user_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='documento',
            field=models.IntegerField(null=True),
        ),
    ]