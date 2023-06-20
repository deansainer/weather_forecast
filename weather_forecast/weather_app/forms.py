from django.forms import ModelForm, TextInput
from . models import *


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['city']
        widgets = {'city': TextInput(attrs={
            'class': 'form-control',
            'city': 'city',
            'id': 'city',
        })}