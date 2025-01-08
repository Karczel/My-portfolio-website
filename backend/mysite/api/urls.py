from rest_framework import routers
from django.urls import path, include
from myapp.api.urls import myapp_router

router = routers.DefaultRouter()

router.registry.extend(myapp_router.registry)

urlpatterns = [
    path('', include(router.urls))
]