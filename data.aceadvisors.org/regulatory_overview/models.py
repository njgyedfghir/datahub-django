from unicodedata import category
from django.db import models
from django.utils.timezone import now
import os


class Region(models.Model):
    country = models.CharField(max_length=100, unique=True, null=True)
    flag_image = models.ImageField(upload_to='country_flags/', null=True, blank=True)
    
    def __str__(self):
        return str(self.country)

    

    

class Year(models.Model):
    current_year = models.IntegerField(
        default=1945,
        choices=[(year, str(year)) for year in range(1945, 2100)]
    )

    def __str__(self):
        return str(self.current_year)
class EndYear(models.Model):
    current_year = models.IntegerField(
        default=1945,
        choices=[(year, str(year)) for year in range(1945, 2025)]
    )

    def __str__(self):
        return str(self.current_year)

class DataRepository(models.Model):
    Data_Name = models.CharField(max_length=100, unique=True, null=True)
    Description = models.TextField(null=True, blank=True, max_length=200)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.Data_Name
def remove_underscore(filename):
    return filename.replace('_', ' ')

def pdf_file_upload_to(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = remove_underscore(base_filename) + file_extension
    return f'posts/{new_filename}'
class NationalStrategies(models.Model):
    TYPES = (
        ("Free", "Free"),
        ("Paid", "Paid"),
    )
    PdfTitle = models.CharField(max_length=100, unique=True, null=True)
    DataRepository = models.ForeignKey(DataRepository, on_delete=models.SET_NULL, null=True)
    Status = models.CharField(choices=TYPES, max_length=100, null=True, default="", blank=False)
    Region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    Year =  models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='regulatory_framework/', null=True, blank=True, max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    @property
    def get_filename(self):
        name = ""
        for i in self.file.name.split("/")[1:]:
            name += i
        return name

    @property
    def get_short_filename(self):
        if len(self.get_filename) > 36:
            return self.get_filename[0: 30] + '...'
        return self.get_filename
    def __str__(self):
         if self.PdfTitle:
            return self.PdfTitle
         else:
            return "Untitled"


class BusinessStrategy(models.Model):
    OPTIONS = (
        ("Directives", "Directives"),
        ("Proclamations", "Proclamations"),
        ("Regulations", "Regulations"),
        ("Manual", "Manual"),
       
    )
    TYPES = (
        ("Free", "Free"),
        ("Paid", "Paid"),
    )
    PdfTitle = models.CharField(max_length=100, unique=True, null=True)
    category = models.CharField(choices=OPTIONS, max_length=100, null=True, default="", blank=False)
    DataRepository = models.ForeignKey(DataRepository, on_delete=models.SET_NULL, null=True)
    Status = models.CharField(choices=TYPES, max_length=100, null=True, default="", blank=False)
    Region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    Year =  models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='regulatory_framework', null=True, blank=True, max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    @property
    def get_filename(self):
        name = ""
        for i in self.file.name.split("/")[1:]:
            name += i
        return name

    @property
    def get_short_filename(self):
        if len(self.get_filename) > 36:
            return self.get_filename[0: 30] + '...'
        return self.get_filename
    def __str__(self):
         if self.PdfTitle:
            return self.PdfTitle
         else:
            return "Untitled"

class OtherStudie(models.Model):
    TYPES = (
        ("Free", "Free"),
        ("Paid", "Paid"),
    )
    PdfTitle = models.CharField(max_length=100, unique=True, null=True)
    DataRepository = models.ForeignKey(DataRepository, on_delete=models.SET_NULL, null=True)
    Status = models.CharField(choices=TYPES, max_length=100, null=True, default="", blank=False)
    Region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    Year =  models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='regulatory_framework/', null=True, blank=True, max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    @property
    def get_filename(self):
        name = ""
        for i in self.file.name.split("/")[1:]:
            name += i
        return name

    @property
    def get_short_filename(self):
        if len(self.get_filename) > 36:
            return self.get_filename[0: 30] + '...'
        return self.get_filename
    def __str__(self):
         if self.PdfTitle:
            return self.PdfTitle
         else:
            return "Untitled"

    

    
class ImportantLinks(models.Model):
    Organization_name = models.CharField(max_length=100, unique=True, null=True)
    Description = models.TextField(null=True, blank=True, max_length=200)
    link = models.CharField(max_length=500, null=True, default="", blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    @property
    def get_short_link(self):
        if len(self.link) > 100:
            return self.link[:97] + '...'
        return self.link
    
    @property
    def get_shoreter_link(self):
        if len(self.get_short_link) > 36:
            return self.link[:30] + '...'
        return self.link

    def __str__(self):
        return self.Organization_name
