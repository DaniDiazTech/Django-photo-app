'''Photo app Forms'''

from django import forms
from django.forms import fields

from .models import Photo

class CreatePhotoForm(forms.ModelForm):
    
    class Meta:
        model = Photo

        fields = ('title', 'description', 'image', 'tags')

    
class UpdatePhotoForm(forms.ModelForm):
    
    class Meta:
        model = Photo

        fields = ('title', 'description')
        