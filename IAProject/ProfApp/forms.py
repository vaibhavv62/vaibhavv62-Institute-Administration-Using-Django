from django import forms
from django.db.models import fields
from .models import Prof

class ProfModelForm(forms.ModelForm):
    class Meta:
        model = Prof
        fields = '__all__'

    def clean_salary(self):
        user_entered_salary = self.cleaned_data['salary']
        if user_entered_salary<0:
            raise forms.ValidationError('Salary must be greater than 0...')
        else:
            return user_entered_salary