# Generated by Django 3.1.2 on 2021-04-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_token', '0003_auto_20210407_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetoken',
            name='device_key',
            field=models.TextField(max_length=350),
        ),
    ]