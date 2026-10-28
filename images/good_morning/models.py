from django.db import models

class GoodMorning(models.Model):
    image = models.ImageField(upload_to='morning_gallery')

# Create your models here.
