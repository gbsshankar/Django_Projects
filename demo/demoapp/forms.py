from django import forms
from .models import demomodel
# creating a form
class demoform(forms.ModelForm):
    # creating a meta class
    class Meta:
        # specify model to be used
        model=demomodel
        # specify fields to be used
        fields=[
            "title",
            "description",
       ]