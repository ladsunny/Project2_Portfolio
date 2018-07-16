from django.db import models

# Create your models here.
class holding(models.Model):
    image = models.ImageField(upload_to='images/')
    company = models.CharField(max_length=50)
    weight = models.DecimalField(null=True,max_digits=5,decimal_places=2)
