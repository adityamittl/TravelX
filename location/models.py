from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class current_location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    longitude = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user)
    

class previous_locations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    longitude = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user)


class location(models.Model):
    name = models.CharField(max_length= 150)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    
class location_images(models.Model):
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'location_images')