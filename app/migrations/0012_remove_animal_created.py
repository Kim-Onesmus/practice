# Generated by Django 2.2.25 on 2022-02-23 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_animal_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='created',
        ),
    ]