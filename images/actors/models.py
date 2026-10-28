from django.db import models

class moviews(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photu/')

class molly(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics/')