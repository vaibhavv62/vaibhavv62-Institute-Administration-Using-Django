from django import forms
from django.db.models import fields
from .models import Subject

class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'