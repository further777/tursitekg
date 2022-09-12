# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
from .views import RegionViewSet, ContactViewSet, RouteViewSet, Kind_transportViewSet, HousingViewSet, FoodViewSet, LocationViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'region', RegionViewSet, basename='ragion')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'route', RouteViewSet, basename='route')
router.register(r'kind_transport', Kind_transportViewSet, basename='kind_transport')
router.register(r'housing', HousingViewSet, basename='housing')
router.register(r'food', FoodViewSet, basename='food')
router.register(r'location', LocationViewSet, basename='location')

urlpatterns = router.urls