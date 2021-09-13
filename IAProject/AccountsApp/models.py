from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self,mobile_no,email,is_student,is_professor,password,**other_fields):
        if not mobile_no:
            raise ValueError('You must provide mobile number!')
        if not email:
            raise ValueError('You must provide an email address!')

        email = self.normalize_email(email)
        user = self.model(mobile_no=mobile_no,email=email,is_student=is_student,
                          is_professor=is_professor,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,mobile_no,email,is_student,is_professor,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(mobile_no,email,is_student,is_professor,password,**other_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    mobile_no = models.CharField(max_length=13,unique=True)
    email = models.EmailField(max_length=64,unique=True)
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    #
    forgot_pw_token = models.CharField(max_length=128,blank=True)
    is_active = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=128,blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'mobile_no'
    REQUIRED_FIELDS = ['email','is_student','is_professor']

    def __str__(self):
        return f'{self.mobile_no},{self.email}'
