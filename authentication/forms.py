from django import forms
from .models import Notice


class NoticeForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Notice
        fields = ('title','desc', 'image')