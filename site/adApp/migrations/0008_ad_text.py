# Generated by Django 5.0.1 on 2024-01-18 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adApp', '0007_media_delete_mediatest'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
