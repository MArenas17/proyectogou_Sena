# Generated by Django 4.1.3 on 2023-04-19 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servigou', '0020_alter_user_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='documento',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
