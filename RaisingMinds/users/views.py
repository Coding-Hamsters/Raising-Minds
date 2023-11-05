from typing import Any
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import login as user_login,logout,authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .token import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages


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

                # set up email comfimation to signup
                current_site = get_current_site(request)
                subject = "Confirm Your Email"
                message = render_to_string('users/confirmationEmail.html',{
                    'user': newUser,
                    'domain':current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(newUser.pk)),
                    'token': generate_token.make_token(newUser)

                })

                email = EmailMessage(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [newUser.email]

                )


                email.send()

                return HttpResponse('<h1>We Send You a Confirmation Email</h1>')
            
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

# active the user after confirm the comfirmation mail
def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()

        user_login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('login')
    else:
        return HttpResponse('<h1>Activation Fail!</h1>')