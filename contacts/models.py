from django.db import models
# from django.contrib.gis.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)

