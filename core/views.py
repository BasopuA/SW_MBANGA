from django.shortcuts import render
from events.models import Event  # Import from events app
from datetime import datetime

def home(request):
    current_year = datetime.now().year
    events = Event.objects.filter(event_date__year=current_year)[:10]
    return render(request, 'core/home.html', {
        'events': events,
        'current_year': current_year
    })