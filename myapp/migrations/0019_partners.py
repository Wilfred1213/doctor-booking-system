# Generated by Django 5.0 on 2024-01-14 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000, null=True)),
                ('logos', models.ImageField(null=True, upload_to='partners_images')),
            ],
        ),
    ]