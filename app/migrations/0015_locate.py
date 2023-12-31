# Generated by Django 4.0.2 on 2022-03-07 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_delete_items_delete_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
