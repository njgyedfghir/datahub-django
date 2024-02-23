from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.conf import settings

class DataRepositorySerializer(serializers.ModelSerializer):
   

    class Meta:
        model = DataRepository
        fields = '__all__'
class StartYearSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Year
        fields = '__all__'

class regionSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Region
        fields = ['id', 'country', 'flag_image']

#NationalStrategies model

class NationalStrategiesSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    data_repository_name = serializers.CharField(source='DataRepository.Data_Name')
    Year = serializers.IntegerField(source='Year.current_year', allow_null=True)
    region_name = serializers.CharField(source='Region.country')
    region_image = serializers.ImageField(source='Region.flag_image')
    pdfs = serializers.SerializerMethodField()

    class Meta:
        model = NationalStrategies
        fields = ['id',  'file_name', 'PdfTitle','file', 'data_repository_name', 'Status','region_name', 'region_image',  'Year', 'updated', 'created', 'pdfs']

    def get_file_name(self, obj):
        return obj.file.name.split("/")[-1].replace("_", " ")

    def get_pdfs(self, obj):  # Change parameter name to obj
        # Assuming `Status` field determines if it's free or paid
        is_free = obj.Status == 'Free'
        
        base_url = settings.BASE_URL
        full_url = f"{base_url}{obj.file.url}"
        return {
            'title': obj.file.name.split("/")[-1].replace("_", " "),
            'downloadLink': full_url,
            'isFree': is_free
        }
        
class FilesSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = NationalStrategies
        fields = ['file_name']

    def get_file_name(self, obj):
        # Get the file name from the full file URL
        file_url = obj.file.url
        return file_url.split('/')[-1].replace("_", " ") if file_url else None

class myCategorySerializer(serializers.Serializer):
    category = serializers.CharField()
    count = serializers.IntegerField()
    files = FilesSerializer(many=True)


#test rf
class RFSerializer(serializers.ModelSerializer):
   
    DataRepository__Data_Name=serializers.CharField(source='DataRepository.Data_Name')
    Region__country=serializers.CharField(source='Region.country')
    Region__flag_image=serializers.ImageField(source='Region.flag_image')
    


    class Meta:
        model = BusinessStrategy
        fields = ['id', 'category', 'file', 'created', 'DataRepository__Data_Name', 'Region__country',  'Region__flag_image ' ]

#RegulatoryFramework model
    
class RegulatoryFrameworkSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    data_repository_name = serializers.CharField(source='DataRepository.Data_Name')
    region_name = serializers.CharField(source='Region.country')
    region_image = serializers.ImageField(source='Region.flag_image')
    Year = serializers.IntegerField(source='Year.current_year', allow_null=True)
    #EYear = serializers.IntegerField(source='EYear.current_year', allow_null=True)
    pdfs = serializers.SerializerMethodField()
    

    class Meta:
        model = BusinessStrategy
        fields = ['id', 'category','PdfTitle', 'file_name', 'file', 'data_repository_name', 'Status', 'region_name' , 'region_image', 'Year', 'updated', 'created', 'pdfs']

   
    def get_file_name(self, obj):
        # Get the file name from the full file URL
        file_url = obj.file.url
        return obj.file.name.split("/")[-1].replace("_", " ")
    
    def get_pdfs(self, obj):  # Change parameter name to obj
        # Assuming `Status` field determines if it's free or paid
        is_free = obj.Status == 'Free'
        
        base_url = settings.BASE_URL
        full_url = f"{base_url}{obj.file.url}"
        return {
            'title': obj.file.name.split("/")[-1].replace("_", " "),
            'downloadLink': full_url,
            'isFree': is_free
        }
class FileSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = BusinessStrategy
        fields = ['file_name']

    def get_file_name(self, obj):
        # Get the file name from the full file URL
        file_url = obj.file.url
        return file_url.split('/')[-1].replace("_", " ") if file_url else None

class CategorySerializer(serializers.Serializer):
    category = serializers.CharField()
    count = serializers.IntegerField()
    files = FileSerializer(many=True)



#ImportantLinks model
class OtherStudiesSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    data_repository_name = serializers.CharField(source='DataRepository.Data_Name')
    Year = serializers.IntegerField(source='Year.current_year', allow_null=True)
    region_name = serializers.CharField(source='Region.country')
    region_image = serializers.ImageField(source='Region.flag_image')
    pdfs = serializers.SerializerMethodField()

    class Meta:
        model = OtherStudie
        fields = ['id',  'file_name','PdfTitle', 'file', 'data_repository_name', 'Status','region_name', 'region_image',  'Year', 'updated', 'created','pdfs']

    def get_file_name(self, obj):
        return obj.file.name.split("/")[-1].replace("_", " ")
    
    def get_pdfs(self, obj):  # Change parameter name to obj
        # Assuming `Status` field determines if it's free or paid
        is_free = obj.Status == 'Free'
        
        base_url = settings.BASE_URL
        full_url = f"{base_url}{obj.file.url}"
        return {
            'title': obj.file.name.split("/")[-1].replace("_", " "),
            'downloadLink': full_url,
            'isFree': is_free
        }


    
class ImportantLinksSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = ImportantLinks
        fields = '__all__'



