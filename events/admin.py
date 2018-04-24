from django.contrib import admin

# Register your models here.

from .models import Event, Event_Participation

admin.site.register(Event)
admin.site.register(Event_Participation)
