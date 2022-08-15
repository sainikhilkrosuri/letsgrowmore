from django.db import models


# Create your models here.
class activity(models.Model):
    acc = models.CharField(max_length=100)
    default = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)


class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    gender = models.CharField(max_length=10)
    java = models.BooleanField()
    python = models.BooleanField()
    other = models.BooleanField()


class SubmitForm(models.Model):
    pin = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    ms = models.CharField(max_length=1)
    ds = models.CharField(max_length=1)
    java = models.CharField(max_length=1)
