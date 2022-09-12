from rest_framework import serializers
from .models import Region, Location, Route, Kind_transport, Food, Housing, Contact
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'picture', 'description']
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'mobile', 'telegram', 'home']
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'distance_air', 'picture',  'region', 'description']
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'time', 'num_tran', 'description', 'kind_tran', 'location']
class Kind_transportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind_transport
        fields = ['id', 'name', 'quantity_place', 'price', 'description']
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'kitchen', 'description', 'price_day', 'location', 'picture']
class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housing
        fields = ['id', 'name', 'adress', 'pic_cart', 'url', 'price', 'contact', 'location', 'description']