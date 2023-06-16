from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField('protfolio/')