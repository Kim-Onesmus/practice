# Generated by Django 2.2.25 on 2022-02-14 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220214_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='Animal_ame',
            new_name='Animal_name',
        ),
    ]