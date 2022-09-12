from django.contrib.auth.models import User
from accounts.models import userProfile
from rest_framework import viewsets
from .permissions import IsOwnerProfileOrReadOnly
from .models import Region, Location, Route, Kind_transport, Food, Housing, Contact
from .serializers import FoodSerializer, HousingSerializer, Kind_transportSerializer, LocationSerializer, RegionSerializer, ContactSerializer, RouteSerializer
class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
class ContactViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]
    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)
class LocationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]
    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)
class RouteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]
    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)
class Kind_transportViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Kind_transport.objects.all()
    serializer_class = Kind_transportSerializer
    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)
class HousingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]
    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)
class FoodViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]
    def perform_create(self, serializer):
        user = User.objects.get(username=self.request.user)
        userP = userProfile.objects.get(user=user)
        serializer.save(user=userP)