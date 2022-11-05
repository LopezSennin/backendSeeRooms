from email.policy import default
import uuid
from django.db import models

# Create your models here.
class Usersapp(models.Model):
    id_user_app = models.IntegerField(primary_key = True)
    fullName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phoneNumber = models.IntegerField()
    password = models.CharField(max_length=200)

class Place(models.Model):
    id_place = models.UUIDField(default = uuid.uuid4, unique = True, editable = False, primary_key = True)
    owner = models.ForeignKey(Usersapp, on_delete = models.CASCADE)
    price = models.IntegerField()

class Characteristics(models.Model):
    place = models.ForeignKey(Place , on_delete = models.CASCADE)
    Characteristic = models.CharField(max_length=200)

class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete = models.CASCADE)
    photo = models.URLField()

class Ubication(models.Model):
    place = models.ForeignKey(Place, on_delete = models.CASCADE)
    address = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

class Rent(models.Model):
    id_rent = models.UUIDField(default = uuid.uuid4, unique = True, editable = False, primary_key = True)
    renter = models.ForeignKey(Usersapp, on_delete = models.CASCADE)
    place = models.ForeignKey(Place, on_delete = models.CASCADE)
    date = models.DateField()