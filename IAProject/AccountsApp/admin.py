from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    # A]View
    ordering = ('start_date',)
    list_display = ['mobile_no','email','is_email_verified','start_date','is_student','is_professor','is_staff','is_active','forgot_pw_token','email_verification_token']
    search_fields = ('mobile_no','email')#Search Functionality
    list_filter = ['is_superuser','is_staff','is_active']#,'mobile_no','email']#Filter Functionality

    # B]Change/Update
    readonly_fields = ('start_date',)
    fieldsets = (
        ('Account',{'fields':('mobile_no','email','password')}),
        ('Permissions',{'fields':('is_student','is_professor','is_superuser','is_staff','is_active')}),
        ('Personal Info',{'fields':('start_date',)})
    )

    # C]Add
    add_fieldsets = (
        (None,{'classes':('wide',),
               'fields':('mobile_no','email','password1','password2','is_staff','is_active')}
         ),
    )

admin.site.register(CustomUser,CustomUserAdmin)