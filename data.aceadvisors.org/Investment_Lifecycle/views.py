from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from regulatory_overview.models import *

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from django.db.models import Count
# Create your views here.
def Pre(request):
    Test = Preimplementation.objects.all()
    context = {"Test": Test}
    return render(request, "Test/Test_form.html", context=context)

def index(request):
    return redirect("/")

class PreimplementationList(generics.ListAPIView):
    serializer_class = PreimplementationSerializer
    def get_queryset(self):
        return Preimplementation.objects.all()
    
class ImplementationList(generics.ListAPIView):
    serializer_class = ImplementationSerializer
    def get_queryset(self):
        return Implementation.objects.all()
    
class OperationList(generics.ListAPIView):
    serializer_class = OperationSerializer
    def get_queryset(self):
        return Operation.objects.all()