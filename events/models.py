from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

def year_check(datevalue):
    datevalue_year = datevalue.year
    if not (1900 <= datevalue.year <= 2099):
        raise ValidationError('%s is not a realistic year...' % datevalue_year)

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    start_date = \
        models.DateField(
            blank=True,
            null=True,
            validators=[year_check]
        )
    end_date = \
        models.DateField(
            blank=True,
            null=True,
            validators=[year_check]
        )
    full_description = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    possible_short_term_camping_nights = models.PositiveSmallIntegerField(blank=True,null=True)
    possible_long_term_camping_nights = models.PositiveSmallIntegerField(blank=True,null=True)
    possible_service_hours = models.FloatField(blank=True,null=True)
    camping_trip = models.NullBooleanField(blank=True)
    outing_non_camping = models.NullBooleanField(blank=True)
    service_project = models.NullBooleanField(blank=True)
    meeting = models.NullBooleanField(blank=True)
    misc_troop_activity = models.NullBooleanField(blank=True)
    event_participants = models.ManyToManyField(User, through='Event_Participation')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_name


class Event_Participation(models.Model):
    YES = 'YES'
    MAYBE = 'MAYBE'
    NOTGOING = 'NOTGOING'
    GOING_CHOICES = (
        (YES, 'Yes'),
        (MAYBE, 'Maybe'),
        (NOTGOING, 'No'),
    )

    scout = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    going = models.CharField(max_length=8, choices=GOING_CHOICES, blank=True)
    reason_not_going = models.CharField(max_length=255, blank=True, null=True)
    is_providing_transportation = models.NullBooleanField(blank=True)
    is_lead_scout = models.NullBooleanField(blank=True)
    is_lead_asm = models.NullBooleanField(blank=True)
    is_two_deep_adult_leader = models.NullBooleanField(blank=True)
#
    arrived_date = models.DateField(blank=True,null=True)
    departed_date = models.DateField(blank=True,null=True)
    actual_short_term_camping_nights = models.PositiveSmallIntegerField(blank=True,null=True)
    actual_long_term_camping_nights = models.PositiveSmallIntegerField(blank=True,null=True)
    actual_service_hours = models.FloatField(blank=True,null=True)
#
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# -------------------------------------------------

# departure time
# departure location
# return time
# return location

# Event
#     food
#     clothing
#     shelter
# 
#     equipment
#     money
#     transportation
# 
#     who
#     what
#     when
#     where
#     why
#     how

