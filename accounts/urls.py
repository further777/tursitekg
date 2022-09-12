from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserProfileListCreateView, userProfileDetailView
# router = DefaultRouter()
# router.register(r'all-profiles/', UserProfileListCreateView, basename='')
# router.register(r'profile/<int:pk>/',userProfileDetailView, basename='')
# urlpatterns = router.urls
urlpatterns = [
    #gets all user profiles and create a new profile
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),
]