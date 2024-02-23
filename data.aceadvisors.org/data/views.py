from django.http import Http404
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from regulatory_overview.models import *
from .models import *
import json


from django.http import FileResponse
from django.conf import settings
from django.http import HttpResponseNotFound
import os

from django.shortcuts import render

from django.http import JsonResponse

# views.py

from django.shortcuts import render, redirect
#from .models import UploadedContent
#from .forms import UploadContentForm

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import viewsets

class SubmitFormAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SubmitFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Frontslider(request):
    sliders = frontslider.objects.all()
    serializer = frontsliderSerializer(sliders, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def Frontsliders(request, pk):
    sliders = frontslider.objects.get(id=pk)
    serializer = frontsliderSerializer(sliders, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def overview(request):
    overviews = Overview.objects.all()
    serializer = OverviewSerializer(overviews, many=True)
    
    return Response(serializer.data)
@api_view(['GET'])
def dataindicator(request):
    dataindicators = DataIndicator.objects.all()
    serializer = DataIndicatorSerializer(dataindicators, many=True)
    
    return Response(serializer.data)
@api_view(['GET'])
def regulatoryoverview(request):
    regulatoryoverviews = RegulatoryOverview.objects.all()
    serializer = RegulatoryOverviewSerializer(regulatoryoverviews, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def PostView(request):
    posts = post.objects.all()
    serializer = postSerializer(posts, many=True, context={'request': request})
    return Response(serializer.data)




def submit_form_view(request):
    if request.method == 'POST':
        # Handle the form submission here
        # Extract form data from the request
        comments = request.POST.get('comments')  # Replace 'comments' with the name of your textarea field

        # Process the form data (you can perform validation, save to the database, etc.)
        # For demonstration purposes, we'll simply return a success response
        # You can replace this with your actual processing logic

        # Assuming the form submission is successful
        # You can return a JSON response with a success message
        return JsonResponse({'status': 'success', 'message': 'Form submitted successfully!'})

    # If the request method is not POST, render the template with the form
    return render(request, 'your.html')  # Replace 'your_template.html' with the actual template file name

def confirm_form(request):
    if request.method == 'POST':
        # Assuming your form has 'name' and 'email' fields, you can access the data like this:
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        # Do whatever processing you need to with the form data (e.g., saving to the database)
        # ...

        # Return a JSON response with a success message
        response_data = {
            'status': 'success',
            'message': 'Form submitted successfully!',
        }
        return JsonResponse(response_data)

    # If the request method is not POST or any other error occurs, return an error JSON response
    response_data = {
        'status': 'error',
        'message': 'Error submitting the form. Please try again later.',
    }
    return JsonResponse(response_data, status=400)  # Use status=400 to indicate a bad request






def read_file(request):
    # Code to read the file content or generate its content
    file_content = "This is the content of the file. this me"

    return render(request, 'datapage/file_view.html', {'file_content': file_content})
    #return render(request, 'continue_reading.html')

def sample(request):
    # Code to read the file content or generate its content
    file_content = "This is the content of the file. this me why people are careless"

    return render(request, 'datapage/blur.html', {'file_content': file_content})
    #return render(request, 'continue_reading.html')
    
def continue_reading(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        father_name = request.POST.get('father_name')
        cell_phone = request.POST.get('cell_phone')
        email = request.POST.get('email')

        # Validate the form data (if needed)
        if not name or not father_name or not cell_phone or not email:
            return render(request, 'datapage/continue_reading.html', {'error_message': "Please fill in all required fields."})

        # Save the data or perform any desired action
        # ...

        # Redirect to a confirmation page or another appropriate view
        return redirect('rest_of_file')  # Replace 'confirmation' with the URL name for your confirmation page

    # For GET request, render the continue_reading.html template
    return render(request, 'datapage/continue_reading.html')

def rest_of_file(request):
    # Code to fetch or generate the remaining content of the file
    rest_of_file_content = "This is the rest of the file content."

    return render(request, 'datapage/rest_of_file.html', {'rest_of_file_content': rest_of_file_content})

def download_file(request):
    #file_path = os.path.join(settings.MEDIA_ROOT, 'Melat_CV.pdf')
    file_name = 'ATI IT Team KnowledgeExp Sharing Workshop_Schedule_Dec2728_2022.pdf'  # The name you want the downloaded file to have
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    #response = FileResponse(open(file_path, 'rb'))
    #response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    #return response
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    else:
        return HttpResponseNotFound("File not found.")

def index(request):
    #paids = Paid.objects.all()
    indicators = Indicator.objects.all()
   # ns = NationalStrategies.objects.all()[0: 4]
    il = ImportantLinks.objects.all()[0:4]
    context = {
        "indicators": indicators,
        #"ns": ns,
        "il": il,
        
    }
    return render(request, "datapage/home.html", context=context)

def underconstruction(request):
    return render(request, "datapage/under_construction.html")

def search(request):
    searchquery = request.GET.get("search")
    # vector = SearchVector('name', weight="A") + SearchVector('keywords', weight="B")
    data_results = AceData.objects.filter(
        Q(name__contains=searchquery) | Q(keywords__icontains=searchquery)
    )
    indicator_results = Indicator.objects.filter(indicator__contains=searchquery)
    files = AceFile.objects.filter(file_name__icontains=searchquery)
    context = {
        "length": len(data_results) + len(indicator_results) + len(files),
        "data_results": data_results,
        "indicators_results": indicator_results,
        "files": files,
        "q": searchquery
    }
    print(context)
    return render(request, "datapage/search.html", context=context)

def graph_page(request, title):
    try:
        data = AceData.objects.get(slug=title)
    except ObjectDoesNotExist as e:
        raise Http404
    additional_data = AceData.objects.all()
    context = {
        "graph_title": data.name,
        "years": json.loads(data.years_list,),
        "numbers": json.loads(data.data_numbers),
        "data": data,
        "additional": additional_data,
        "view_more": len(additional_data)>6
    }
    return render(request, "datapage/graph_page.html", context=context)

def indicator_page(request, indicator):
    try:
        i = Indicator.objects.get(indicator__icontains=indicator)
        indicators = AceData.objects.filter(indicator=i)
    except ObjectDoesNotExist as e:
        raise Http404
    context = {
        "page_title": f"{i.indicator} Indicator",
        "list": indicators,
        "indicator": indicator.lower()
    }
    return render(request, "datapage/indicator_list_page.html", context=context)

def error_404(request, exception):
    return render(request, "datapage/404.html")
