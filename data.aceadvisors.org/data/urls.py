from django.urls import path, include
from . import views as views

from django.urls import path
from .views import download_file

from .views import read_file,continue_reading,rest_of_file,sample

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from .views import SubmitFormAPIView
urlpatterns = [
    path("", views.index, name='home-link'),
    path("search/", views.search, name='search-link'),
    path("graph/<str:title>", views.graph_page, name='graph-link'),
    path("indicators/<str:indicator>", views.indicator_page, name="indicator-link"),
    path("underconstruction/", views.underconstruction, name='construction-link'),
    path('download/', download_file, name='download'),
    path('read_file/', read_file, name='read_file'),
    path('continue_reading/',continue_reading,name='continue_reading'),
    path('rest_of_file/', rest_of_file, name='rest_of_file'),
    path('sample/', sample, name='sample'),
    path('confirm_forms/', views.confirm_form, name='confirm_forms'),

    #path('upload/', views.upload_content, name='upload_content'),
   # path('content/', views.content_list, name='content_list'),


    #path('paid/<str:pk>/', views.paid, name ='paid'),

   path('Sliders', views.Frontslider, name="Sliders"),
   path('Sliders/<str:pk>', views.Frontsliders, name="Slider"),
   path('Views', views.overview, name="Views"),
   path('DataIndicators', views.dataindicator, name="DataIndicators"),
   path('RegulatoryOverviews', views.regulatoryoverview, name="RegulatoryOverviews"),
   path('Article', views.PostView, name="Article"),
   path('Submit/', SubmitFormAPIView.as_view(), name="submit_data"),
    

]


if settings.DEBUG:
    # Serve uploaded media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
