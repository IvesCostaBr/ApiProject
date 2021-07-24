from rest_framework import viewsets, permissions, authentication
from .serializers import CostumerSerializer
from .models import Costumer



class CostumerViewSet(viewsets.ModelViewSet):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer

    permission_classes = (permissions.IsAuthenticated,)
   




