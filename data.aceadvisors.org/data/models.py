from email.policy import default
from django.db import models
from django.utils.timezone import now
from django_countries.fields import CountryField
from django.utils.html import format_html

class SubmitForm(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Mobile_Number = models.CharField(max_length=15)
class Region(models.Model):
    country = models.CharField(max_length=100, unique=True, null=True)
    flag_image = models.ImageField(upload_to='country_flags/', null=True, blank=True)
    
    def __str__(self):
        return str(self.country)

    

    

class Year(models.Model):
    start_year = 1945
    current_year = models.IntegerField(default=start_year, choices=[(year, str(year)) for year in range(start_year, 2025)])

    def __str__(self):
        return str(self.current_year)


class frontslider(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.Title
class Overview(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.Title
class DataIndicator(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.Title
class RegulatoryOverview(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    Region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    Year =  models.IntegerField(default=1945, choices=[(year, str(year)) for year in range(1945, 2025)])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.Title
    
class category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    

    def __str__(self):
        return self.name

class post(models.Model):
    OPTIONS = (
        ("Free", "Free"),
        ("Paid", "Paid"),
    )

    Title = models.CharField(max_length=100, unique=True)
    Description = models.TextField(null=True, blank=True)
    Status = models.CharField(choices=OPTIONS, max_length=100, null=True, default="", blank=False)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey('subcategory', on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='posts/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

    

class subcategory(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.get_combined_name

    @property
    def get_combined_name(self):
        return f"{self.category.name} / {self.name}"

class Indicator(models.Model):
    indicator = models.CharField(max_length=100, null=True, default="", blank=False)
    banner_img = models.ImageField(upload_to="images/", null=True, blank=False, default="")

    def __str__(self):
        return f"{self.indicator} indicator"


class AceData(models.Model):
    name = models.CharField(max_length=100, null=True, default="", blank=False)
    data = models.FileField(upload_to='fileData/', null=True, blank=True)
    data_excel = models.FileField(upload_to='fileData/', null=True, blank=True)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    years_list = models.TextField(null=True, blank=True, default="")
    data_numbers = models.TextField(null=True, blank=True, default="")
    keywords = models.TextField(null=True, blank=True, default="")
    date_created = models.DateTimeField(default=now, editable=False)
    slug = models.SlugField(default="", null=True, blank=True)

    def __str__(self):
        return self.name

class AceFile(models.Model):
    FILE_TYPES = (
        ("EXCEL", "Excel"),
        ("CSV", "CSV (Comma Separated Values)"),
        ("PDF", "PDF"),
        ("OTHER", "other"),
    )
    file_name = models.CharField(max_length=100, null=True, default="", blank=False)
    file_type = models.CharField(max_length=10, choices=FILE_TYPES, default="", null=True, blank=False)
    file = models.FileField(upload_to='fileData/', null=True, blank=True)
    data = models.ForeignKey(AceData, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.file_name

    @property
    def get_filename(self):
        name = ""
        for i in self.file.name.split("/")[1:]:
            name += i
        return name