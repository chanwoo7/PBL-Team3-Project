# Generated by Django 5.0.1 on 2024-01-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adApp', '0004_rename_price_ad_ad_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='ad/%Y%m%d')),
                ('desc', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
