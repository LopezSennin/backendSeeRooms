from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UsersappSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usersapp
        fields = ['url', 'id_user_app', 'fullName', 'email', 'phoneNumber', 'password']

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['url', 'id_place', 'owner', 'price']

class CharacteristicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Characteristics
        fields = ['url', 'place', 'Characteristic']

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['url', 'place', 'photo']

class UbicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ubication
        fields = ['url', 'place', 'address', 'neighborhood', 'city', 'state']

class RentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rent
        fields = ['url', 'id_rent', 'renter', 'place', 'date']