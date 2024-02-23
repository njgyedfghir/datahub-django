from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import PreimplementationList
from .views import ImplementationList
from .views import OperationList



urlpatterns = [
    path('/', views.index),
    path('Preimplementaion', PreimplementationList.as_view(), name='Preimplmentation'),
    path('Implementation', ImplementationList.as_view(), name='Implementation'),
    path('Operation', OperationList.as_view(), name='Operation'),
    #path('Strategy', NationalStrategiesList.as_view(), name='Strategy'),
]