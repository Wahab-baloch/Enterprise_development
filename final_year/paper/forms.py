from django import forms
from .models import vlog

class BlogForm(forms.ModelForm):
    class Meta:
        model = vlog
        fields = '__all__'
