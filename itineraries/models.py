from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
            return self.name

class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
            return self.name + ' - ' + self.destination.name

class Itinerary(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    startDate = models.DateField()
    finishDate = models.DateField()
    destinations = models.ManyToManyField(Destination)
    accommodations = models.ManyToManyField(Accommodation)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse('itinerary_detail', kwargs={"id": self.id})