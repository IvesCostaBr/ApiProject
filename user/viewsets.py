from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework import decorators as rest_api
from rest_framework import viewsets, permissions, authentication
from .serializers import CostumerSerializer
from .models import Costumer



class CostumerViewSet(viewsets.ModelViewSet):
    serializer_class = CostumerSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete', 'patch'] #metodos suportados

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
    
    def partial_update(self,request, *args, **kwargs):
        return super(CostumerViewSet, self).partial_update(request, *args, **kwargs)

    def update(self,request, *args, **kwargs):
        return super(CostumerViewSet, self).update(request, *args, **kwargs)

    def list(self,request, *args, **kwargs):
        return super(CostumerViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(CostumerViewSet, self).retrieve(request, *args, **kwargs)

    @rest_api.action(methods=['post'], detail=True)
    def change_password(self, request, pk=None): #change password action
        resp = ''
        costumer = Costumer.objects.get(id=pk)
        if (self.request.POST.get('new_password', None)):
            costumer.set_password(self.request.POST['new_password'])
            resp = 'updated'
        else:
            resp = 'error'

        return Response({"status":resp})



   




