# Generated by Django 5.0.1 on 2024-02-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0015_customer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]
