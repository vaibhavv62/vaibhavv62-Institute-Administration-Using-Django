from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class CustomUser(AbstractBaseUser):
    mobile_no = models.CharField(max_length=13)
    email = models.EmailField()
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
