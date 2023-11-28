# Generated by Django 4.2.7 on 2023-11-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('credit', models.IntegerField(default=0)),
                ('description', models.TextField(default='')),
                ('semester', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
            ],
        ),
    ]