from email.policy import default
import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key = True)
    fullName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phoneNumber = models.IntegerField()
    password = models.CharField(max_length=200)

class Place(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False, primary_key = True)
    owner = models.ManyToManyField(User)
    price = models.IntegerField()

class Characteristics(models.Model):
    id = models.ManyToManyField(Place)
    Characteristic = models.CharField(max_length=200)

class Photo(models.Model):
    place = models.ManyToManyField(Place)
    photo = models.URLField()

class Ubication(models.Model):
    place = models.ManyToManyField(Place)
    address = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

class Rent(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False, primary_key = True)
    renter = models.ManyToManyField(User)
    place = models.ManyToManyField(Place)
    date = models.DateField()