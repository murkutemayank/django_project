from django import forms
from App1.models import uploadedfile
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = uploadedfile
        fields = ['title', 'file']

