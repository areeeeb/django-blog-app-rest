# I CREATED THIS ONLY FOR IMPLEMENTING API

from django.urls import path, include
from rest_framework import routers

from .api_views import UserViewSet, ProfileViewSet, login

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
