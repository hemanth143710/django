from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.homepage, name='home'),
    path("about", views.about, name='about'),
    path("data", views.data, name='data'),
    path("plot", views.plot, name='plot'),
    path("homepage", views.homepage, name='homepage'),

    
]
