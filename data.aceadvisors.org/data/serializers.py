from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class frontsliderSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = frontslider
        fields = '__all__'
class OverviewSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Overview
        fields = '__all__'
class DataIndicatorSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = DataIndicator
        fields = '__all__'
class RegulatoryOverviewSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = RegulatoryOverview
        fields = '__all__'
class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Add the PDF file URL to the representation
        representation['pdfLink'] = self.context['request'].build_absolute_uri(instance.file.url) if instance.file else None

        return representation

class SubmitFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitForm
        fields = ['First_name', 'Last_name', 'Email', 'Mobile_Number']