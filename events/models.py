# events/models.py
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()  # Actual event date
    date_posted = models.DateTimeField(auto_now_add=True)  # Auto-set on creation
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    @property
    def event_year(self):
        return self.event_date.year
    
    class Meta:
        ordering = ['-event_date']  # Newest events first

    def __str__(self):
        return self.title

class EventPhoto(models.Model):
    event = models.ForeignKey(Event, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_photos/')
    
    def __str__(self):
        return f"Photo for {self.event.title}"
