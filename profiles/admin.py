from django.contrib import admin
from .models import Profile, Address
from django.contrib.auth.models import User

admin.site.register(Profile)
admin.site.register(Address)

# --------------------------------------

# from Django Design Patterns and Best Practices:

# class UserProfileInline(admin.StackedInline):
#     model = Profile
# 
# class UserAdmin(admin.UserAdmin):
#     inlines = [UserProfileInline]
# 
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)