# Generated by Django 5.0 on 2024-01-05 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_department_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='image',
            field=models.ImageField(null=True, upload_to='department_images'),
        ),
    ]