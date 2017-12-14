
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Address(models.Model):
    street1 = models.CharField(max_length=50)
    street2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.street1

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# Django Design Patterns and Best Practices:
# user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)    
    
#     bio = models.TextField(max_length=500, blank=True)
#     biography = models.TextField(max_length=100, blank=True)
#     location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    join_troop_date = models.DateTimeField('date joined troop', null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Profile._meta.fields]

    def __str__(self):
        return (
            self.user.last_name 
            + ", " + self.user.first_name 
            + " " + str(self.middle_name)
        )
#         return (self.middle_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# -------------------------------------------------

