from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('campaign/',views.campaign,name='campaign'),
    path('index/',views.index,name='Home')
]
