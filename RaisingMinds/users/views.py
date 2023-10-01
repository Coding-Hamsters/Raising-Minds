from typing import Any
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import login,logout

# Create your views here.
def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(username,password1,email)

        if password1 == password2:

            if User.objects.filter(email = email).exists():
                return HttpResponse('email is exist!')
            
            else:
                newUser = User.objects.create_user(email,username,password1)
                newUser.save()

                return redirect('login')
            
        else:
            return HttpResponse('password are not same!')

    return render(request,'users/signup.html')

def login(request):
    return render(request,'users/login.html')