# Generated by Django 4.2.7 on 2023-11-26 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='year',
        ),
    ]
