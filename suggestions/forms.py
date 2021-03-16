from django import forms
from .models import Suggestions



class CreateSuggestion(forms.ModelForm):
    class Meta:
        model = Suggestions
        fields = ['title', 'content']
        