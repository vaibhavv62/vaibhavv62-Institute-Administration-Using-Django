from django import forms
from django.db.models import fields
from .models import Branch

class BranchModelForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'

    def clean_intake(self):
        user_entered_intake = self.cleaned_data['intake']
        if user_entered_intake<30:
            raise forms.ValidationError('You need at least 30 seats to start branch...')
        else:
            return user_entered_intake

    def clean_college_fees(self):
        user_entered_college_fees = self.cleaned_data['college_fees']
        if user_entered_college_fees < 0:
            raise forms.ValidationError('College Fees must be greater than 0...') 
        else:
            return user_entered_college_fees

    def clean_exam_fees(self):
        user_entered_exam_fees = self.cleaned_data['exam_fees']
        if user_entered_exam_fees < 0:
            raise forms.ValidationError('Exam Fees must be greater than 0...') 
        else:
            return user_entered_exam_fees