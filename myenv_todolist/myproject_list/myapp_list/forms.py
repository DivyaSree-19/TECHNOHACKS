# forms.py
from django import forms
from .models import MyappList

class MyForm(forms.ModelForm):
    class Meta:
        model = MyappList
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter Title here...',
                'style': 'width: 300px;'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter description here...',
                'rows': 6,
                'cols': 43,
            }),
            'status': forms.Select(attrs={
                'style': 'width: 200px; height: 40px;'  # Adjust the width and height as needed
            }),
        }



