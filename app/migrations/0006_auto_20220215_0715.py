# Generated by Django 2.2.25 on 2022-02-15 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220214_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='animal',
            name='Img',
            field=models.ImageField(upload_to=''),
        ),
    ]
