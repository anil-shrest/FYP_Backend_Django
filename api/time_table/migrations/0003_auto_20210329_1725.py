# Generated by Django 3.1.2 on 2021-03-29 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_table', '0002_auto_20210327_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timetable',
            options={'ordering': ['created_at']},
        ),
    ]