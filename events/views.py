from django.shortcuts import render
from .models import Event

def search_events(request):
    year = request.GET.get('year')
    events = Event.objects.filter(event_date__year=year)
    return render(request, 'core/home.html', {
        'events': events,
        'current_year': year
    })