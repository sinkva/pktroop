from django.contrib import admin

# Register your models here.

from .models import Patrol, Patrol_Membership

admin.site.register(Patrol)
admin.site.register(Patrol_Membership)
