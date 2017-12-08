from django.contrib import admin

# Register your models here.

from .models import Profile, Address
# , Patrol, Patrol_Membership

admin.site.register(Profile)
admin.site.register(Address)
# admin.site.register(Patrol)
# admin.site.register(Patrol_Membership)
