from typing import Any
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import login as user_login,logout,authenticate

# Create your views here.
def signup(request):

    # get the data from signup.html form
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # check the password and confirm passwords are equal
        if password1 == password2:

            # check the email is exists or not
            if User.objects.filter(email = email).exists():
                return HttpResponse('email is exist!')
            
            else:
                # create a new user
                newUser = User.objects.create_user(email,username,password1)
                newUser.is_active = False
                newUser.save()



                return redirect('login')
            
        else:
            return HttpResponse('password are not same!')

    return render(request,'users/signup.html')

def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')

        user = authenticate(request,email = email,password = password1)

        if user is not None:
            user_login(request,user)
            return redirect('home')

        else:
            return HttpResponse('<h1>password or email not correct</h1>')

    return render(request,'users/login.html')