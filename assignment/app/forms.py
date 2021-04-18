from django import forms

from .models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('username','date_of_file_upload','file')
