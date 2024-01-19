# Generated by Django 5.0 on 2024-01-06 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_doctor_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, null=True)),
                ('image', models.ImageField(null=True, upload_to='doctor_images')),
                ('description', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
