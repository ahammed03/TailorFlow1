# Generated by Django 5.0.1 on 2024-02-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0019_alter_customer_tailor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
