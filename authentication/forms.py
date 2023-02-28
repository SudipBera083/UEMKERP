from django import forms
from .models import Notice, Teacher, Authentication

class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = Authentication
        fields = "__all__"
        
class NoticeForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Notice
        fields = "__all__"
        labels ={'image':''}

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields ="__all__"
        labels={'image':""}