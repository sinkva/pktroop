from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.forms.models import modelform_factory

from .models import Patrol, Patrol_Membership

def index(request):
    all_patrols = Patrol.objects.all()
    context = {'all_patrols': all_patrols}
    return render(request, 'patrols/index.html', context)
    
def detail(request, patrol_id):
    patrol = get_object_or_404(Patrol, pk=patrol_id)
    related_patrol_membership = \
        Patrol_Membership.objects \
        .filter( patrol = patrol ) \
        .order_by('-date_joined') \
        .select_related()
    formfac = modelform_factory(Patrol, fields=('patrol_name',))
    return render(
        request, 
        'patrols/detail.html', 
        {   'patrol': patrol, 
            'related_patrol_membership': related_patrol_membership,
            'formfac': formfac,
        }
    )

def update(request, patrol_id):
    patrol = get_object_or_404(Patrol, pk=patrol_id)
    return render(request, 'patrols/update.html', {'patrol': patrol})

def updatesave(request, patrol_id):
    if 'update' in request.POST:
        patrol = get_object_or_404(Patrol, pk=patrol_id)
        patrol.patrol_name = request.POST['patrol_name']
        patrol.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('patrols:detail', args=(patrol_id,)))
    else:
        return HttpResponseRedirect(reverse('patrols:detail', args=(patrol_id,)))


