from django.urls import path
from . import views

urlpatterns =[
    path('',views.LandingInterface, name='home')
]

