from django.shortcuts import render
from .serializers import UserSignupSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import CustomUser
from .forms import SignUpForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.contrib.auth.hashers import check_password

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import CustomUser

def signup_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        role_name = request.POST.get('roles')

        if password == cpassword:
            if role_name:
                # Create a new CustomUser instance and save it to the database
                new_user = CustomUser.objects.create(
                    email=email,
                    username=username,
                    password=make_password(password),
                    role=role_name  # Assign the role name to the user
                )
                return redirect('login')
            else:
                msg = 'Please select a role'
                return render(request, 'signup.html', {'msg': msg})
        else:
            msg = 'Password and Confirm Password do not match'
            return render(request, 'signup.html', {'msg': msg})
    else:
        return render(request, 'login.html')

from django.contrib.auth.hashers import check_password


def login_view(request):
    try:
        email = request.session['email']
        # Check if the user exists with the given email
        try:
            user = CustomUser.objects.get(email=email)
            return render(request, 'inventory.html')
        except CustomUser.DoesNotExist:
            # If the user does not exist, redirect to login page
            return render(request, 'login.html')
    except KeyError:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = CustomUser.objects.get(email=email)
                # Check if the password matches
                if check_password(password, user.password):
                    request.session['email'] = email
                    return render(request, 'inventory.html')
                else:
                    msg = 'Password does not match'
                    return render(request, 'login.html', {'msg': msg})
            except CustomUser.DoesNotExist:
                msg = 'First register yourself'
                return render(request, 'signup.html', {'msg': msg})
        else:
            return render(request, 'login.html')
