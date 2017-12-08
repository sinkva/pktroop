from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Profile
from django.views.generic import ListView, DetailView

from .models import Profile
from patrols.models import Patrol, Patrol_Membership

from django.db.models.functions import Lower

def index(request):
    all_profiles = Profile.objects.order_by(Lower('user__last_name'))
    context = {'all_profiles': all_profiles}
    return render(request, 'profiles/index.html', context)

def detail(request, Profile_id):
    this_profile = get_object_or_404(Profile, pk=Profile_id)
    related_patrol_membership = \
        Patrol_Membership.objects \
        .filter( scout = this_profile.user ) \
        .order_by('-date_joined') \
        .select_related()
    return render(
        request, 
        'profiles/detail.html', 
        {   'profile': this_profile, 
            'related_patrol_membership': related_patrol_membership
        } 
    )

def update(request, Profile_id):
    this_profile = get_object_or_404(Profile, pk=Profile_id)
    return render(request, 'profiles/update.html', { 'profile': this_profile })

def updatesave(request, Profile_id):
    if 'update' in request.POST:
        profile = get_object_or_404(Profile, pk=Profile_id)
        profile.user.first_name = request.POST['first_name']
        profile.middle_name = request.POST['middle_name']
        profile.user.last_name = request.POST['last_name']
        profile.user.save()
        profile.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('profiles:detail', args=(Profile_id,)))
    else:
        return HttpResponseRedirect(reverse('profiles:detail', args=(Profile_id,)))
