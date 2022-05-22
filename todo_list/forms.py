from typing import List
from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'item','placeholder': 'Add item'}),
        }