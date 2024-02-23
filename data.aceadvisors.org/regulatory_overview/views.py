from __future__ import print_function
#from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from django.db.models import Count
from django.http import JsonResponse
from django.db.models import Q
from Investment_Lifecycle.models import *
from Investment_Lifecycle.serializers import *
from data.models import RegulatoryOverview
from data.serializers import RegulatoryOverviewSerializer
from datetime import datetime, timedelta
from itertools import chain
from django.views import View

def index(request):
    return redirect("/")



class SearchResultView(View):
    def get(self, request, *args, **kwargs):
        searchstring = self.kwargs.get('searchstring')  # Access the URL parameter
       # yearstring = self.kwargs.get('yearstring')
        reg = Region.objects.all()
        reg_serialized = regionSerializer(reg, many=True)
        
        dr_results = DataRepository.objects.filter(Q(Data_Name__icontains=searchstring))
        dr_serialized = DataRepositorySerializer(dr_results, many=True)
        
        if searchstring:
            rf_results = BusinessStrategy.objects.filter(Q(PdfTitle__icontains=searchstring) |
                                                            Q(DataRepository__Data_Name__icontains=searchstring) |
                                                            Q(category__icontains=searchstring) |
                                                           Q(Region__country__icontains=searchstring))  # Filter based on file name)
        

        else:
            rf_results = BusinessStrategy.objects.all()
        rf_serialized = RegulatoryFrameworkSerializer(rf_results, many=True)
        
        # Filter based on the presence of searchstring
        if searchstring:
            ns_results = NationalStrategies.objects.filter(Q(PdfTitle__icontains=searchstring) |
                                                          Q(DataRepository__Data_Name__icontains=searchstring) |
                                                           Q(Region__country__icontains=searchstring))
        else:
            ns_results = NationalStrategies.objects.all()
        ns_serialized = NationalStrategiesSerializer(ns_results, many=True)

        if searchstring:
            ot_results = OtherStudie.objects.filter(Q(PdfTitle__icontains=searchstring) |
                                                    Q(DataRepository__Data_Name__icontains=searchstring) |
                                                          Q(Year__current_year__icontains=searchstring) |
                                                           Q(Region__country__icontains=searchstring))
        else:
            ot_results = OtherStudie.objects.all()
        ot_serialized = OtherStudiesSerializer(ot_results, many=True)
        il = ImportantLinks.objects.all()
        il_serialized = ImportantLinksSerializer(il, many=True)
        
        preimp = Preimplementation.objects.all()
        preimp_serialized = PreimplementationSerializer(preimp, many=True)
        
        imp = Implementation.objects.all()
        imp_serialized = ImplementationSerializer(imp, many=True)
        
        opr = Operation.objects.all()
        opr_serialized = OperationSerializer(opr, many=True)
        
        ro_results = RegulatoryOverview.objects.all()
        ro_serialized = RegulatoryOverviewSerializer(ro_results, many=True)

        context = {
            "reg ": reg_serialized.data ,
            "dr_results ": dr_serialized.data ,
            "rf_results ": rf_serialized.data ,
            "ns_results ": ns_serialized.data ,
            "ot_results ": ot_serialized.data ,
            "il": il_serialized.data, 
            "preimp": preimp_serialized.data,
            "imp": imp_serialized.data,
            "opr": opr_serialized.data,
            "ro_results": ro_serialized.data,
        }

        return JsonResponse(context, status=status.HTTP_200_OK)
    
class FilterResultView(View):
    def get(self, request, *args, **kwargs):
        searchstring = self.kwargs.get('searchstring')  # Access the URL parameter
        
        reg = Region.objects.all()
        reg_serialized = regionSerializer(reg, many=True)
        
        dr_results = DataRepository.objects.filter(Q(Data_Name__icontains=searchstring))
        dr_serialized = DataRepositorySerializer(dr_results, many=True)
        
        if searchstring:
            rf_results = BusinessStrategy.objects.filter(Q(PdfTitle__icontains=searchstring) |
                                                            Q(DataRepository__Data_Name__icontains=searchstring) |
                                                            Q(category__icontains=searchstring) |
                                                            Q(Year__current_year__icontains=searchstring) |
                                                           Q(Region__country__icontains=searchstring)) 
                                                          # Q(StartYear__current_year=searchstring) ) # Filter based on file name)
        else:
            rf_results = BusinessStrategy.objects.all()
        rf_serialized = RegulatoryFrameworkSerializer(rf_results, many=True)
        
        # Filter based on the presence of searchstring
        if searchstring:
            ns_results = NationalStrategies.objects.filter(Q(PdfTitle__icontains=searchstring) |
                                                          Q(DataRepository__Data_Name__icontains=searchstring) |
                                                          Q(Year__current_year__icontains=searchstring) |
                                                           Q(Region__country__icontains=searchstring))
        else:
            ns_results = NationalStrategies.objects.all()
        ns_serialized = NationalStrategiesSerializer(ns_results, many=True)

        if searchstring:
            ot_results = OtherStudie.objects.filter(Q(PdfTitle__icontains=searchstring) |
                                                    Q(DataRepository__Data_Name__icontains=searchstring) |
                                                          Q(Year__current_year__icontains=searchstring) |
                                                           Q(Region__country__icontains=searchstring))
        else:
            ot_results = OtherStudie.objects.all()
        ot_serialized = OtherStudiesSerializer(ot_results, many=True)
        il = ImportantLinks.objects.all()
        il_serialized = ImportantLinksSerializer(il, many=True)
        
        preimp = Preimplementation.objects.all()
        preimp_serialized = PreimplementationSerializer(preimp, many=True)
        
        imp = Implementation.objects.all()
        imp_serialized = ImplementationSerializer(imp, many=True)
        
        opr = Operation.objects.all()
        opr_serialized = OperationSerializer(opr, many=True)
        
        ro_results = RegulatoryOverview.objects.all()
        ro_serialized = RegulatoryOverviewSerializer(ro_results, many=True)

        context = {
            "reg ": reg_serialized.data ,
            "dr_results ": dr_serialized.data ,
            "rf_results ": rf_serialized.data ,
            "ns_results ": ns_serialized.data ,
            "ot_results ": ot_serialized.data ,
            "il": il_serialized.data, 
            "preimp": preimp_serialized.data,
            "imp": imp_serialized.data,
            "opr": opr_serialized.data,
            "ro_results": ro_serialized.data,
        }

        return JsonResponse(context, status=status.HTTP_200_OK)
from django.views.decorators.http import require_GET

@require_GET
def get_filter_options(request):
    # Assuming sectors, regions, start years, and end years are fetched from models or other sources dynamically
    sector_options = DataRepository.objects.all()
    serialized_options = [{'id': option.id, 'value': option.Data_Name} for option in sector_options]
    return JsonResponse(serialized_options, safe=False)
@require_GET
def get_region_options(request):
    # Assuming sectors, regions, start years, and end years are fetched from models or other sources dynamically
    region_options = Region.objects.all()
    serialized_options = [{'id': option.id, 'value': option.country} for option in region_options]
    return JsonResponse(serialized_options, safe=False)
@require_GET
def get_year_options(request):
    # Assuming sectors, regions, start years, and end years are fetched from models or other sources dynamically
    year_options = Year.objects.all()
    serialized_options = [{'id': option.id, 'value': option.current_year} for option in year_options]
    return JsonResponse(serialized_options, safe=False)
def filter_data(request):
    # Get filter parameters from request
    filter_param = request.GET.get('filter_param', None)
    
    # Filter data based on the parameter
    if filter_param:
        filtered_data = BusinessStrategy.objects.filter(DataRepository__Data_Name=filter_param)
    else:
        filtered_data = BusinessStrategy.objects.all()

    # Serialize data
    serialized_data = RegulatoryFrameworkSerializer(filtered_data, many=True).data
    
    return JsonResponse(serialized_data, safe=False)
def searchfilterview(request,regionFilter,dataTypeFilter,startYearFilter,endYearFilter):

        # Start building the query for filtering instances
        query = Q()

        # Apply filters based on provided parameters
        if regionFilter:
            query &= Q(Region__country=regionFilter) 
                      

        if dataTypeFilter:
            query &= Q(DataRepository__Data_Name=dataTypeFilter)  # Replace 'data_type_field' with the actual field name in your model

        if startYearFilter:
            query &= Q(StartYear__gte=startYearFilter)  # Replace 'start_year_field' with the actual field name in your model

        if endYearFilter:
            query &= Q(EndYear__lte=endYearFilter)  # Replace 'end_year_field' with the actual field name in your model

        # Perform the filtering on RegulatoryFramework instances
        rf_filtered_results = BusinessStrategy.objects.filter(query)
        rf_serialized = RegulatoryFrameworkSerializer(rf_filtered_results, many=True).data

        # Perform the filtering on NationalStrategies instances
        ns_filtered_results = NationalStrategies.objects.filter(query)
        ns_serialized = NationalStrategiesSerializer(ns_filtered_results, many=True).data

        context = {
            "rf_results": rf_serialized,
            "ns_results": ns_serialized,
        }

        # Return the serialized results as a JSON response
        return JsonResponse(context, safe=False)
def filter(request):
    filter = request.GET.get('filter') if request.GET.get('filter') != None else ''
    regionFilter = request.GET.get('regionFilter', '')
    dataTypeFilter = request.GET.get('dataTypeFilter', '')
    startYearFilter = request.GET.get('startYearFilter', '')
    endYearFilter = request.GET.get('endYearFilter', '')

    reg = Region.objects.filter(
    Q(flag_image__contains=filter),
    country__contains=regionFilter
    )
    reg_serialized = regionSerializer(reg, many=True)
    
    print(f"searchquery: {filter}, regionFilter: {regionFilter}")
    dr_results = DataRepository.objects.filter( 
        Q(Description__icontains=filter) ,
        Data_Name__icontains=dataTypeFilter, )
    dr_serialized = DataRepositorySerializer(dr_results, many=True)
    try:
       startYearFilter = int(startYearFilter)
    except (ValueError, TypeError):
       startYearFilter = None
       print("Invalid startYearFilter value")

    try:
       endYearFilter = int(endYearFilter)
    except (ValueError, TypeError):
       endYearFilter = None
       print("Invalid startYearFilter value")

       print(f"startYearFilter: {startYearFilter}, endYearFilter: {endYearFilter}")
    rf_results = BusinessStrategy.objects.filter(
        StartYear__gte=startYearFilter if startYearFilter is not None else 0,
        EndYear__lte=endYearFilter if endYearFilter is not None else 9999 
    )
    rf_serialized = RegulatoryFrameworkSerializer(rf_results, many=True)
    ns_results = NationalStrategies.objects.filter(
        StartYear__gte=startYearFilter if startYearFilter is not None else 0,
        EndYear__lte=endYearFilter if endYearFilter is not None else 9999 
    )
    ns_serialized = NationalStrategiesSerializer(ns_results, many=True)
        
    context = {
        
        "reg ": reg_serialized.data ,
        "dr_results ": dr_serialized.data ,
        "rf_results ": rf_serialized.data ,
        "ns_results ": ns_serialized.data ,
        "regionFilter": regionFilter ,
        "dataTypeFilter": dataTypeFilter, 
        "startYearFilter": startYearFilter ,
        "endYearFilter": endYearFilter ,
        
    }
    return JsonResponse(context, safe=False)

def Test(request):
    Test = ImportantLinks.objects.all()
    context = {"Test": Test}
    return render(request, "Test/Test_form.html", context=context)
class OtherStudiesList(generics.ListAPIView):
    serializer_class = OtherStudiesSerializer
    def get_queryset(self):
        return OtherStudie.objects.all()
class NationalStrategiesList(generics.ListAPIView):
    serializer_class = NationalStrategiesSerializer
    def get_queryset(self):
        return NationalStrategies.objects.all()
class region(generics.ListAPIView):
    serializer_class = regionSerializer
    def get_queryset(self):
        return Region.objects.all()  
class DataRepositoryList(generics.ListAPIView):
    serializer_class = DataRepositorySerializer
    def get_queryset(self):
        return DataRepository.objects.all()  
    
class CategoryofStartegyList(generics.ListAPIView):
    serializer_class = myCategorySerializer

    def get_queryset(self):
        # Get distinct categories with their counts
        categories_with_counts = NationalStrategies.objects.values('category').annotate(
            count=Count('file')
        )

        # Combine categories with counts and associated files
        result = []
        for category_with_count in categories_with_counts:
            category = category_with_count['category']
            count = category_with_count['count']
            files = NationalStrategies.objects.filter(category=category)
            serializer_data = {
                'category': category,
                'count': count,
                'files': files
            }
            result.append(serializer_data)

        return result


class RegulatoryFrameworkList(generics.ListAPIView):
    serializer_class = RegulatoryFrameworkSerializer
    def get_queryset(self):
        return BusinessStrategy.objects.all()
from django.http import JsonResponse


def staoption(request):
    selected_option = request.GET.get('selectedOption', 'ALL')

    if selected_option == 'ALL':
        results = NationalStrategies.objects.all().order_by('-created')
    elif selected_option == 'Latest':
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        results = NationalStrategies.objects.filter(updated__gte=today).order_by('-created')
    elif selected_option == 'Last Week':
        last_week = datetime.now() - timedelta(weeks=1)
        results = NationalStrategies.objects.filter(updated__gte=last_week).order_by('-created')
    elif selected_option == 'Last Month':
        last_month = datetime.now() - timedelta(days=3)
        results = NationalStrategies.objects.filter(updated__gte=last_month).order_by('-created')
    

    serialized_results = NationalStrategiesSerializer(results, many=True)
    return JsonResponse({'data': serialized_results.data})


class CategoryWithFilesList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        # Get distinct categories with their counts
        categories_with_counts = BusinessStrategy.objects.values('category').annotate(
            count=Count('file')
        )

        # Combine categories with counts and associated files
        result = []
        for category_with_count in categories_with_counts:
            category = category_with_count['category']
            count = category_with_count['count']
            files = BusinessStrategy.objects.filter(category=category)
            serializer_data = {
                'category': category,
                'count': count,
                'files': files
            }
            result.append(serializer_data)

        return result
from django.conf import settings 
def get_file_counts(request):
    national_strategies_counts = NationalStrategies.objects.values('Region__country', 'Region__flag_image','PdfTitle').annotate(file_count=Count('file'))
    regulatory_framework_counts = BusinessStrategy.objects.values('Region__country', 'Region__flag_image', 'PdfTitle').annotate(file_count=Count('file'))
    other_studies_counts = OtherStudie.objects.values('Region__country', 'Region__flag_image', 'PdfTitle').annotate(file_count=Count('file'))
    
    # Combine counts for common countries
    file_counts = {}
    for item in national_strategies_counts:
        region = item['Region__country']
        flag_image = item['Region__flag_image']  # Retrieve the flag image URL
        flag_image_url = settings.MEDIA_URL + str(flag_image)  # Construct the full image URL
        file_counts[region] = file_counts.get(region, {'file_count': 0, 'flag_image_url': flag_image_url})
        file_counts[region]['file_count'] += item['file_count']
    for item in regulatory_framework_counts:
        region = item['Region__country']
        flag_image = item['Region__flag_image']  # Retrieve the flag image URL
        flag_image_url = settings.MEDIA_URL + str(flag_image)  # Construct the full image URL
        file_counts[region] = file_counts.get(region, {'file_count': 0, 'flag_image_url': flag_image_url})
        file_counts[region]['file_count'] += item['file_count']
    for item in other_studies_counts:
        region = item['Region__country']
        flag_image = item['Region__flag_image']  # Retrieve the flag image URL
        flag_image_url = settings.MEDIA_URL + str(flag_image)  # Construct the full image URL
        file_counts[region] = file_counts.get(region, {'file_count': 0, 'flag_image_url': flag_image_url})
        file_counts[region]['file_count'] += item['file_count']

    data = [{'country': region, 'file_count': file_count['file_count'], 'flag_image_url': file_count['flag_image_url']} for region, file_count in file_counts.items()]
    
    
    return JsonResponse(data, safe=False)
    

@api_view(['GET'])
def importantlinks(request):
    links = ImportantLinks.objects.all()
    serializer = ImportantLinksSerializer(links, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def importantlink(request, pk):
    links = ImportantLinks.objects.get(id=pk)
    serializer = ImportantLinksSerializer(links, many=False)
    return Response(serializer.data)



def getyears(request):
    # Get the choices for StartYear and EndYear from the model
    start_year_choices = BusinessStrategy._meta.get_field('StartYear').choices
    end_year_choices = BusinessStrategy._meta.get_field('EndYear').choices

    # Extract the years from the choices
    start_years = [choice[0] for choice in start_year_choices]
    end_years = [choice[0] for choice in end_year_choices if choice[0] is not None]

    # Combine and remove duplicates
    years = list(set(start_years + end_years))

    # Sort the years in descending order
    years.sort(reverse=True)

    return JsonResponse({'years': years})

def count_files_by_region(request):
    if request.method == 'GET':
        country_name = request.GET.get('country')

        try:
            region = Region.objects.get(country=country_name)
            files = NationalStrategies.objects.filter(Region=region)
            file_count = files.count()
            return JsonResponse({'file_count': file_count})
        except Region.DoesNotExist:
            return JsonResponse({'error': 'Region not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=400)