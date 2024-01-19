# Generated by Django 5.0 on 2024-01-02 17:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(choices=[('Surgery Department', 'Surgery Department'), ('Outpatient', 'Outpatient'), ('Inpatient', 'Inpatient'), ('Intensive Care Unit', 'Intensive Care Unit'), ('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Psychiatry', 'Psychiatry'), ('Radiology', 'Radiology'), ('Laboratory', 'Laboratory'), ('Pharmacy', 'Pharmacy'), ('Rehabilitation', 'Rehabilitation'), ('Hematology', 'Hematology'), ('Pediatrics', 'Pediatrics'), ('Oncology', 'Oncology'), ('Ophthalmology', 'Ophthalmology')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('8:00 AM - 9:00 AM', '8:00 AM - 9:00 AM'), ('9:00 AM - 10:00 AM', '9:00 AM - 10:00 AM'), ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'), ('11:00 AM - 12:00 PM', '11:00 AM - 12:00 PM'), ('12:00 PM - 1:00 PM', '12:00 PM - 1:00 PM'), ('1:00 PM - 2:00 PM', '1:00 PM - 2:00 PM'), ('2:00 PM - 3:00 PM', '2:00 PM - 3:00 PM'), ('3:00 PM - 4:00 PM', '3:00 PM - 4:00 PM'), ('4:00 PM - 5:00 PM', '4:00 PM - 5:00 PM')], default='8:00 AM - 9:00 AM', max_length=255)),
                ('message', models.TextField(max_length=10000, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.patient')),
            ],
        ),
    ]
