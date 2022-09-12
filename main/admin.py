from django.contrib import admin
from .models import  Region, Location, Route, Kind_transport, Food, Housing, Contact
# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'description']
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'distance_air', 'picture', 'check_tur', 'region', 'description']
    list_filter = ['region']
    search_fields = ['name']
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'telegram', 'home']
    search_fields = ['name', 'email', 'mobile', 'telegram', 'hame']
class FoodAdmin(admin.ModelAdmin):
    list_display = ['kitchen', 'description', 'price_day', 'check_tur', 'location', 'picture']
    list_filter = ['location']
    search_fields = ['kitchen']
class Kind_transportAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity_place', 'price', 'description']
    search_fields = ['name']
class RouteAdmin(admin.ModelAdmin):
    list_display = ['time', 'num_tran', 'description', 'check_tur', 'kind_tran', 'location']
    list_filter = ['kind_tran', 'location']
    search_fields = ['num_tur', 'time']
class HousingAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress', 'pic_cart', 'price', 'url', 'contact', 'check_tur', 'description']
    search_fields = ['name', 'adress']
admin.site.register(Region, RegionAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Kind_transport, Kind_transportAdmin)
admin.site.register(Housing, HousingAdmin)
admin.site.register(Contact, ContactAdmin)