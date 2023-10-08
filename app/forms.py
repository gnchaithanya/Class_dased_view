from django import forms
from  app.models import *

class StudentFrom(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'