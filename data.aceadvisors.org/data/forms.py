# forms.py

from django import forms
from .models import UploadedContent

class UploadContentForm(forms.ModelForm):
    class Meta:
        model = UploadedContent
        fields = ['title', 'category', 'content']
