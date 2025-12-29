from django import forms
from .models import Brief

class BriefForm(forms.ModelForm):
    class Meta:
        model = Brief
        fields = "__all__"
