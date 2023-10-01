from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# method for render index.html
def index(request):
    return render(request,'app/index.html')

def campagin(request):
    return render(request,'app/campagin.html')
