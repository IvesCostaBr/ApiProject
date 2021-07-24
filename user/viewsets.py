from rest_framework import viewsets
from .serializers import CostumerSerializer
from .models import Costumer



class CostumerViewSet(viewsets.ModelViewSet):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer




