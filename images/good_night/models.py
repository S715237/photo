from django.db import models

class GoodNight(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='good_night_images/')

class Diwali(models.Model):
    image = models.ImageField(upload_to='diwali_images/')


class krishnaJanmashtmi(models.Model):
    image = models.ImageField(upload_to='krishna_images/')

class Ganeshchathurthi(models.Model):
    image =models.ImageField(upload_to='ganesh_images/')
    
class Navratri(models.Model):
    image = models.ImageField(upload_to='Navratri_images/')

class christmas(models.Model):
    image = models.ImageField(upload_to='christmas_images/')  

class Login(models.Model):
    name=models.CharField(max_length=23)
    email=models.EmailField()
    password=models.CharField(max_length=23)
     
    
     

