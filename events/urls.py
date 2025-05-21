# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_events, name='search_events'),
    # Add other event-related URLs here if needed
]