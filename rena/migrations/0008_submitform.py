# Generated by Django 4.0.6 on 2022-08-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rena', '0007_alter_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=10)),
                ('ms', models.CharField(max_length=1)),
                ('ds', models.CharField(max_length=1)),
                ('java', models.CharField(max_length=1)),
            ],
        ),
    ]
