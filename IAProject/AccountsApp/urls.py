from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('test/',views.testingView,name='test'),
    path('register/',views.registerView,name='register'),
    #Email Verification
    path('account_activate/<token>/',views.acc_activationView,name='acc_acti'),
    #
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('profile/',views.profileView,name='profile'),
    # path('home/',views.homeView,name='home'),
    #Change Password with Old Password(Authenticated Users)
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'),
         name='password_change'),
    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
    #Forgot Password
    # path('password_reset/',views.passwordResetView,name='password_reset'),
    path('forgot_password/',views.forgotPasswordView,name='forgotpw'),
    path('change_password/<token>/',views.changePasswordView,name='changepw'),

    ]
