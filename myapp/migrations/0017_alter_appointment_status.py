# Generated by Django 5.0 on 2024-01-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('REJECT', 'Reject'), ('ACCEPT', 'Accept'), ('PENDING', 'Pending')], default='PENDING', max_length=50),
        ),
    ]
