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