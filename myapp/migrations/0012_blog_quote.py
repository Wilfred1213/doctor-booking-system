# Generated by Django 5.0 on 2024-01-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='quote',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
