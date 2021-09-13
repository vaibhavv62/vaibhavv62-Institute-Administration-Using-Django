import csv
import os
from django.core.mail import send_mail
from django.conf import settings



def send_forgotpw_email(to,token):
    subject = "Reset Password - Institute Admin"
    message = f"Hello there,\nGreetings of the day!\n\nWe received a request to reset the password for your account for this email address. To initiate the password reset process for your account, click the link below,\n http://127.0.0.1:8000/accounts/change_password/{token}/ \nThanks & Regards,\n\nVaibhav K.,\nCorporate Relations Division,\nInstitute Administration."
    print('sending password reset email')
    send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[to])
    print('forgot pw mail sent')


def send_acc_verification_email(to,token):
    subject = "Activate your account - Institute Admin!"
    message = f"Hello there,\nGreetings of the day!\n\nWarm welcome to Institute Admin Portal. Please activate your Institute Admin account for this email address. To activate your account, please click the link below,\n http://127.0.0.1:8000/accounts/account_activate/{token}/ \n\nThanks & Regards,\n\nVaibhav K.,\nCorporate Relations Division,\nInstitute Administration."
    print('sending password reset email')
    send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[to])
    print('acc activation mail sent')

