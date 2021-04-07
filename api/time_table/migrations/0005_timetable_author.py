# Generated by Django 3.1.2 on 2021-04-04 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('time_table', '0004_auto_20210404_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL),
        ),
    ]
