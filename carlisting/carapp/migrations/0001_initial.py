# Generated by Django 4.0.3 on 2023-06-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=100)),
                ('seller_mobile', models.CharField(max_length=15)),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.DateField()),
                ('condition', models.CharField(choices=[('Poor', 'Poor'), ('Fair', 'Fair'), ('Good', 'Good'), ('Excellent', 'Excellent')], max_length=20)),
                ('asking_price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
