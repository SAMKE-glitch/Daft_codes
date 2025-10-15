"""
Forms for customer app, including camera photo upload.
"""

from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    """Form for validating and saving uploaded camera photos."""
    
    class Meta:
        model = Photo
        fields = ['image']

