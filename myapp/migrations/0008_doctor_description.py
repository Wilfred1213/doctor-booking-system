# Generated by Django 5.0 on 2024-01-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_doctor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
