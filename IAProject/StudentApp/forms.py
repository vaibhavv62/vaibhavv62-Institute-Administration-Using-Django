from django import forms
from django.db.models import fields
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_rn(self):
        user_entered_rn = self.cleaned_data['rn']
        if user_entered_rn<0:
            raise forms.ValidationError('Roll No. must be greater than 0...')
        else:
            return user_entered_rn
    
    def clean_marks(self):
        user_entered_marks = self.cleaned_data['marks']
        if user_entered_marks<0 or user_entered_marks>100:
            raise forms.ValidationError('Marks must be in range of 0 to 100...')
        else:
            return user_entered_marks