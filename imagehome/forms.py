from django import forms
from .models import Image


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()