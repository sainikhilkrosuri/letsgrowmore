# Generated by Django 4.0.6 on 2022-08-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rena', '0002_activity_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
