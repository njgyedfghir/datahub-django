from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import RegulatoryFrameworkList
from .views import CategoryWithFilesList
from .views import NationalStrategiesList
from .views import CategoryofStartegyList
from .views import DataRepositoryList
from .views import region
from .views import OtherStudiesList
from .views import SearchResultView
from .views import FilterResultView
from .views import searchfilterview

#from .views import getyears
#from .views import FrameworkAPIView
urlpatterns = [
    path('/', views.index),
   
    #path('/strategies/', views.strategies, name="strategies"),
    path('Links', views.importantlinks, name="Links"),
     path('Links/<str:pk>', views.importantlink, name="Links"),
     path('Strategy', NationalStrategiesList.as_view(), name='Strategy'),
     path('others', OtherStudiesList.as_view(), name='Strategy'),
     path("filter", views.filter, name="Test"),
     #path('regoption', views.regoption, name='regoption' ),
     path('staoption', views.staoption, name='staoption' ),
     path('Framework', RegulatoryFrameworkList.as_view(), name='Framework'),
     path('file_counts', views.get_file_counts, name='get_file_counts'),
     path('Category', CategoryWithFilesList.as_view(), name='Category'),
     path('myCategory', CategoryofStartegyList.as_view(), name='Category'),
     path('years', views.getyears, name='years'),
     path('searchresult/', SearchResultView.as_view(), name='searchresult'),
     path('Searchresults/<str:searchstring>', SearchResultView.as_view(), name='searchresult'),
     path('Filterresults/<str:searchstring>', FilterResultView.as_view(), name='searchresult'),
     path('search-results/<str:regionFilter>/<str:dataTypeFilter>/<int:startYearFilter>/<int:endYearFilter>/', searchfilterview, name='search_results'),
    #path("search", views.search, name='search-link'),
   # path("region/", region.as_view(), name='region'),
    path('state', region.as_view(), name='state'),

    path('repository', DataRepositoryList.as_view(), name='repository'),
    path("Test/", views.Test, name="Test"),
    path('count-files-by-region/', views.count_files_by_region, name='count_files_by_region'),
    path('get-filter-options/', views.get_filter_options, name='get_filter_options'),
    path('get-region-options/', views.get_region_options, name='get_region_options'),
    path('get-year-options/', views.get_year_options, name='get_year_options'),
    path('filter-data/', views.filter_data, name='filter_data'),
   
    

#path('api/framework/<str:category>/', FrameworkAPIView.as_view(), name='framework-api'),
   

    
    

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    # Serve uploaded media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
