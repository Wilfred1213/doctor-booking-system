# Generated by Django 5.0 on 2024-01-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0002_customuser_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(null=True, upload_to='user_images'),
        ),
    ]
