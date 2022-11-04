from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'fullName', 'email', 'phoneNumber', 'password']

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['url', 'id', 'owner', 'price']

class CharacteristicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Characteristics
        fields = ['url', 'id', 'Characteristic']

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['url', 'id', 'place', 'photo']

class UbicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ubication
        fields = ['url', 'place', 'address', 'neighborhood', 'city', 'state']

class RentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rent
        fields = ['url', 'id', 'renter', 'place', 'date']