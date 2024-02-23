from django.db import models

# Create your models here.
class Preimplementation(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    PDFFile = models.FileField(upload_to='posts/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.Title
class Implementation(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    PDFFile = models.FileField(upload_to='posts/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.Title
class Operation(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    PDFFile = models.FileField(upload_to='posts/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.Title