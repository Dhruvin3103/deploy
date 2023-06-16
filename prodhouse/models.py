from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Portfolio(models.Model):
    CHOICES = (
        ('current', 'current projects'),
        ('past', 'past projects'),
        ('upcoming', 'upcoming projects'),
    )
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="image/portfolio/")
    project_type = models.CharField(max_length=300,choices=CHOICES,default='past')
    def __str__(self):
        return self.name

class Contactus(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    message = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name+' '+self.email
    

class Slave(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    detail = models.CharField(max_length=300,default="")
    role = models.CharField(max_length=300,default="")
    image = models.ImageField(upload_to="image/slave/")

    def __str__(self) -> str:
        return self.name+' '+self.email
    