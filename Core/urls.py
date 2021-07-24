from django.contrib import admin
from django.urls import path, include
from user.viewsets import CostumerViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users/', CostumerViewSet, basename="Costumer")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
