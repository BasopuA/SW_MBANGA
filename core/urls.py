# core/urls.py - ADD SEARCH ROUTE
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]