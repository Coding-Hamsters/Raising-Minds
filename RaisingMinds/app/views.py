from django.shortcuts import render
from django.http import HttpResponse
from users.models import User

# Create your views here.

# method for render index.html
def index(request):
    return render(request,'app/index.html')

def campagin(request):
    return render(request,'app/campagin.html')

def home(request):

    username = request.user.username

    return render(request,'app/home.html',{'username':username})
