from django import forms
from .models import *

class Test(forms.Form):
    title = forms.CharField(max_length=255)