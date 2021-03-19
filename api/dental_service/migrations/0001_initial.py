# Generated by Django 3.1.5 on 2021-02-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.TextField(max_length=150)),
                ('service_detail', models.TextField(max_length=500)),
                ('service_image', models.ImageField(blank=True, upload_to='', verbose_name='service_image')),
            ],
            options={
                'ordering': ['service_title'],
            },
        ),
    ]
