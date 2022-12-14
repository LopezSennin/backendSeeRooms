from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsersappViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usersapp.objects.all()
    serializer_class = UsersappSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Places to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class CharacteristicsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Characteristics to be viewed or edited.
    """
    queryset = Characteristics.objects.all()
    serializer_class = CharacteristicsSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Photos to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class UbicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ubications to be viewed or edited.
    """
    queryset = Ubication.objects.all()
    serializer_class = UbicationSerializer

class RentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Rents to be viewed or edited.
    """
    queryset = Rent.objects.all()
    serializer_class = RentSerializer