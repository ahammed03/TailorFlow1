# Generated by Django 5.0.1 on 2024-02-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tailors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tailoruser',
            name='profile',
            field=models.ImageField(blank=True, default='default/profile-user.png', upload_to='tailor_profiles/'),
        ),
    ]