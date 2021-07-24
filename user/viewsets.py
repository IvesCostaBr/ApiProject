from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework import viewsets, permissions, authentication
from .serializers import CostumerSerializer
from .models import Costumer



class CostumerViewSet(viewsets.ModelViewSet):
    serializer_class = CostumerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete', 'patch']

    def get_queryset(self):
        return Costumer.objects.all()

    def create(self, request, *args, **kwargs):
        costumer = Costumer.objects.create_user(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            cpf=request.POST.get('cpf'),
            email=request.POST['email'], 
            password=request.POST['password'],
        )
        return Response(costumer.values);


   




