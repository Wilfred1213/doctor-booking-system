# Generated by Django 5.0 on 2024-01-02 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_appointment_specialization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(choices=[('8:00 AM - 9:00 AM', '8:00 AM - 9:00 AM'), ('9:00 AM - 10:00 AM', '9:00 AM - 10:00 AM'), ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'), ('11:00 AM - 12:00 PM', '11:00 AM - 12:00 PM'), ('12:00 PM - 1:00 PM', '12:00 PM - 1:00 PM'), ('1:00 PM - 2:00 PM', '1:00 PM - 2:00 PM'), ('2:00 PM - 3:00 PM', '2:00 PM - 3:00 PM'), ('3:00 PM - 4:00 PM', '3:00 PM - 4:00 PM'), ('4:00 PM - 5:00 PM', '4:00 PM - 5:00 PM')], default='8:00 AM - 9:00 AM', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.time'),
        ),
    ]
