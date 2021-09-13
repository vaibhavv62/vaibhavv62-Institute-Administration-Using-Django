from django.shortcuts import render,redirect
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import authenticate,login, logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomPasswordResetForm
from django.http import HttpResponse
import uuid
from . import helper


#Getting Custom User
# from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your views here.
def loginView(request):
    # try:
    if request.method == 'POST':
        mobile_no = request.POST.get('mobile_no')
        password = request.POST.get('password')

        if not mobile_no or not password:
            messages.error(request,'Both Mobile No & Password are required!')
            return redirect('login')

        # user_obj = CustomUser.objects.filter(mobile_no = mobile_no)
        # print('user:',user_obj)
        user_obj = CustomUser.objects.filter(mobile_no = mobile_no).first()
        print('user.first():',user_obj)

        if user_obj is None:
            messages.error(request,'User Not Found!')
            return redirect('login')

        user = authenticate(mobile_no=mobile_no,password=password)
        print(f'authenticate(mobile_no={mobile_no},password={password})')
        print(f'user={user}')
        if user is None:
            if not user_obj.is_active:
                messages.error(request,'Your account is not activated yet, please check your registered email!')
            else:
                messages.error(request,'Invalid Password!')
            return redirect('login')

        login(request,user)
        return render(request,'home.html')
        # return HttpResponse('User Logged In <br> <a href="/accounts/logout/"> <button type="submit" class="btn btn-primary mt-2">LogOut</button> </a>')

    # except Exception as e:
    #     print('Exception Occured-\n', e)
    if request.user.is_authenticated:
        print(request.user,type(request.user))
        print('User already authenthicated')
        messages.warning(request,'You are already logged in!')
        return redirect('home')
    else:
        print('User is not authenticated, loading login page')

    template_name = 'login.html'
    context = {}
    return render(request,template_name,context)

def registerView(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            mobile_no = form.cleaned_data.get('mobile_no')
            email = form.cleaned_data.get('email')
            token = str(uuid.uuid4())

            user_obj = CustomUser.objects.get(mobile_no=mobile_no)
            user_obj.email_verification_token = token
            user_obj.save()
            helper.send_acc_verification_email(email,token)
            return render(request,'acc_activation_mailsent.html')
            # return redirect('login')
    template_name = 'register1.html'
    context = {'form':form}
    return render(request, template_name, context)

def acc_activationView(request,token):
    user_obj = CustomUser.objects.filter(email_verification_token=token).first()
    user_obj.is_active = True
    user_obj.save()
    messages.success(request, 'Your account is activated. You may go ahead and log in now.')
    return redirect('login')

def logoutView(request):
    logout(request)
    return redirect('login')

def forgotPasswordView(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if not CustomUser.objects.filter(email=email).first():
            messages.error(request,'No user found with this email!')
            return redirect('forgotpw')

        to = email
        token = str(uuid.uuid4())

        user_obj = CustomUser.objects.get(email=email)
        user_obj.forgot_pw_token = token
        user_obj.save()
        helper.send_forgotpw_email(to,token)
        messages.success(request,'An email is sent with password reset instructions.')
        return render(request,'resetpasswordmailsent.html')

    template_name = 'forgotpassword.html'
    context = {}
    return render(request, template_name, context)


def changePasswordView(request,token):
    user_obj = CustomUser.objects.filter(forgot_pw_token=token).first()
    print(user_obj.id)
    initial_dict = {'user_id':user_obj.id}
    form = CustomPasswordResetForm(initial = initial_dict)
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user_id = form.cleaned_data.get('user_id')
            print('Data From FE:',password1,password2,user_id)
            user_obj = CustomUser.objects.get(id=user_id)
            user_obj.set_password(password2)
            user_obj.save()
            messages.success(request,'Your password has been changed. You may go ahead and log in now.')
            return redirect('login')

    template_name = 'changepasswordform.html'
    context = {'form':form}
    return render(request, template_name, context)


def profileView(request):
    return HttpResponse('profileView')

def homeView(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)


