# Generated by Django 3.1.2 on 2021-04-04 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('device_token', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetoken',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
