from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="image/portfolio/")

    def __str__(self):
        return self.name

class Contactus(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    message = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name+' '+self.email
