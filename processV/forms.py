# forms.py
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    batch_no = forms.CharField(max_length=100, label='Batch Number')
