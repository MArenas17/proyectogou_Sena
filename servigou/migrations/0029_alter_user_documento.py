# Generated by Django 4.1.3 on 2023-04-20 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servigou', '0028_alter_user_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='documento',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
