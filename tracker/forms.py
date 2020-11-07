from django import forms
from .models import *


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'category','event']


class WellForm(forms.ModelForm):
    class Meta:
        model = Well
        fields = ['field', 'name']


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['name']

