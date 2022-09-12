from contextlib import nullcontext
from re import T
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from accounts.models import userProfile
# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='image/',height_field=None,width_field=None, null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name
class Location(models.Model):
    name = models.CharField(max_length=200)
    distance_air = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='image/',height_field=None,width_field=None, null=True)
    description = models.TextField(null=True)
    check_tur = models.BooleanField(default=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class Kind_transport(models.Model):
    name = models.CharField(max_length=200)
    quantity_place = models.IntegerField()
    description = models.TextField(null=True)
    price = models.IntegerField()
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class Route(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField()
    num_tran = models.IntegerField()
    description = models.TextField(null=True)
    check_tur = models.BooleanField(default=False)
    kind_tran = models.ForeignKey(Kind_transport, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.name
# class Kind_transport(models.Model):
#     name = models.CharField(max_length=200)
#     quantity_place = models.IntegerField()
#     price = models.IntegerField()
class Food(models.Model):
    kitchen=models.TextField()
    description = models.TextField(null=True)
    price_day = models.CharField(max_length=300)
    check_tur = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='image/',height_field=None,width_field=None, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.kitchen
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    home = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class Housing(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    pic_cart = models.ImageField(upload_to='image/',height_field=None,width_field=None, null=True)
    description = models.TextField(null=True)
    url = models.URLField(max_length=500)
    price = models.CharField(max_length=300)
    check_tur = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name