# Generated by Django 4.1.3 on 2023-03-23 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servigou', '0016_servicio_repartidor_alter_servicio_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='Repartidor',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repartidor', to=settings.AUTH_USER_MODEL),
        ),
    ]