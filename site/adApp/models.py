from django.db import models

# Create your models here.


class Adv(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    verified = models.BooleanField()


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    advId = models.ForeignKey('Adv', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=500)
    type = models.CharField(max_length=10)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
