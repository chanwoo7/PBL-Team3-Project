# Generated by Django 5.0.1 on 2024-01-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adApp', '0012_alter_ad_adv_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
