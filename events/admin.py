from django.contrib import admin
from .models import Event, EventPhoto

class PhotoInline(admin.TabularInline):
    model = EventPhoto
    extra = 1
    max_num = 10  # Enforces your 10-photo limit

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    # Only use fields that actually exist in your model
    list_display = ('title', 'author', 'event_date')  # Changed from event_year
    list_filter = ('event_date', 'author')  # Filter by existing fields
    date_hierarchy = 'event_date'  # Adds date navigation
    search_fields = ('title', 'description')