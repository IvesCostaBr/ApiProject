from django.contrib import admin
from django.urls import path, include
from user.viewsets import CostumerViewSet
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
#endpoints
router.register(r'users', CostumerViewSet, basename="Costumer") #Acesso a view de


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'), #urls de auth
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), #urls de auth
]