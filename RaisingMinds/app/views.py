from django.shortcuts import render

# Create your views here.

# method for render index.html
def index(request):
    return render(request,'app/index.html')

def campaign(request):
    return render(request,'app/campaign.html')