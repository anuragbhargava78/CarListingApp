# Generated by Django 4.0.3 on 2023-06-05 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
