from django import forms
from .models import UserAsk
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']