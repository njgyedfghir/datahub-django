from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class PreimplementationSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Preimplementation
        fields = '__all__'

class ImplementationSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Implementation
        fields = '__all__'

class OperationSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Operation
        fields = '__all__'