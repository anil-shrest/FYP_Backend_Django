# Generated by Django 3.1.2 on 2021-05-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_token', '0004_auto_20210407_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetoken',
            name='device_key',
            field=models.TextField(max_length=1000),
        ),
    ]