from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primarykey = True)
    fullName = models.CharField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    phoneNumber = models.IntegerField(null = False, blank = False)
    password = models.CharField(null = False, blank = False)

class Place(models.Model):
    id = models.UUIDField(null = False, blank = False)
    owner = models.ManyToManyField(User)
    price = models.IntegerField(null = False, blank = False)

class Characteristics(models.Model):
    id = models.ManyToManyField(Place)
    Characteristic = models.CharField(null = False, blank = False)

class Photo(models.Model):
    place = models.ManyToManyField(Place)
    photo = models.URLField(null = False, blank = False)

class Ubication(models.Model):
    place = models.ManyToManyField(Place)
    address = models.CharField(null = False, blank = False)
    neighborhood = models.CharField(null = False, blank = False)
    city = models.CharField(null = False, blank = False)
    state = models.CharField(null = False, blank = False)

class Rent(models.Model):
    id = models.UUIDField()
    owner = models.ManyToManyField(User)
    renter = models.ManyToManyField(User)
    place = models.ManyToManyField(Place)
    date = models.DateField(null = False, blank = False)