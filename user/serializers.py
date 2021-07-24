from rest_framework import serializers
from .models import Costumer


class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ['email', 'cpf', 'first_name', 'last_name']