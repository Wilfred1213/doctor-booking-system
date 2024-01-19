# Generated by Django 5.0 on 2024-01-13 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_appointment_treated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=16, null=True)),
                ('message', models.CharField(max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
