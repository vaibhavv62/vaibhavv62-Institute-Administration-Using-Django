from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
from . import helper

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput,label='Enter Password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')

    class Meta():
        model = CustomUser
        fields = ['mobile_no','email','is_student','is_professor']
        labels = {
            'mobile_no':'Mobile Number:',
            'email': 'Email address:',
            'is_student': 'I am a student',
            'is_professor': 'I am a professor'
        }
        error_messages ={
            'mobile_no':{'unique':'Account with this Mobile number already exists.'},
            'email':{'unique':'Account with this email already exists.'}
        }
        widgets = {
            'mobile_no':forms.TextInput(attrs={'placeholder':'e.g. 9876543210'}),
            'email':forms.TextInput(attrs={'placeholder':'e.g. user@domain.com'})
        }

    def clean_mobile_no(self):
        mobile_no = self.cleaned_data.get('mobile_no')
        if len(mobile_no)!=10:
            self.add_error("mobile_no","Mobile No. must contain of exactly 10 digits!")
        return mobile_no

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            password_validation.validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error('password1', error)
        return password1

    def clean(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not password1 or not password2 or password1 != password2:
            self.add_error("password2","Both password must match!")

        return cleaned_data

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class CustomUserCreationForm1(forms.ModelForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['mobile_no','email','is_student','is_professor','password']


class CustomPasswordResetForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput,label='Create New Password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')
    user_id = forms.CharField(widget=forms.HiddenInput)

    def clean_password1(self):
        print('clean_password1 got called')
        password1 = self.cleaned_data.get('password1')
        try:
            password_validation.validate_password(password1)
        except forms.ValidationError as error:
            self.add_error('password1', error)
        return password1

    def clean(self):
        print('clean got called')
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not password1 or not password2 or password1 != password2:
            self.add_error("password2","Both password must match!")

        return cleaned_data
