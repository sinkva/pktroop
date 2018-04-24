from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.forms.models import modelform_factory
from django.forms.models import modelformset_factory
from django.forms import inlineformset_factory

from .models import Event, Event_Participation, User

from django.contrib.auth.decorators import login_required

from .forms import EventForm, Event_ParticipationForm
from django.utils import timezone

# -------------------------------------------------
from django.core import serializers
from django.forms.models import model_to_dict
# -------------------------------------------------
from django.db.models.functions import Lower
from django.core.exceptions import ObjectDoesNotExist



def index(request):
    all_events = Event.objects.all()
    context = {'all_events': all_events}
    return render(request, 'events/index.html', context)


@login_required
def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    form = Event_ParticipationForm(instance=event)
    related_event_participation = \
        Event_Participation.objects \
        .filter( event = event ) \
        .select_related()
    return render(
        request, 
        'events/detail.html', 
        {   'event': event, 
            'related_event_participation': related_event_participation,
            'form': form, }
    )


@login_required
def dump_all_data(request):
    data = serializers.serialize( "python", Event.objects.all() )
    return render(  request, 
                    'events/dump_all_data.html', 
                    {'data': data,}
                 )


@login_required
def update(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    form = EventForm(instance=event)
    return render(request, 'events/update.html', {'event': event, 'form': form})


@login_required
def updatesave(request, event_id):
    if 'update' in request.POST:
        event = get_object_or_404(Event, pk=event_id)
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
#             event.event_name = request.POST['event_name']
#             event.start_date = request.POST['start_date']
#             event = form.save()
#             event = form.save(commit=False)
#             form.save(commit=False)
#             form.updated_at = timezone.now()
            form.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('events:detail', args=(event_id,)))
        else: # form did not validate
            return render(request, 'events/update.html', {'event': event, 'form': form})
    else: # 'cancel' button
        return HttpResponseRedirect(reverse('events:detail', args=(event_id,)))

        
@login_required
def participationsave(request, event_id):
    if 'update' in request.POST:
        event = get_object_or_404(Event, pk=event_id)
        form = Event_ParticipationForm(request.POST, instance=event)
        return HttpResponseRedirect(reverse('events:detail', args=(event_id,)))
    else: # 'cancel' button
        return HttpResponseRedirect(reverse('events:detail', args=(event_id,)))


@login_required
def dbaccess(request, event_id):
#         scout = models.ForeignKey(User, on_delete=models.CASCADE)
#         event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     e = request.GET.get('event')
    s = request.POST.get('scout')
    c = request.POST.get('chk')
    if c == 'true' : # box was checked, add scout to event
        if Event_Participation.objects.filter(scout_id=s, event_id=event_id).count() == 0:
            ep = Event_Participation(scout_id=s, event_id=event_id)
            ep.save()
    else: # box was un-checked, delete scout from event
        if Event_Participation.objects.filter(scout_id=s, event_id=event_id).count() >= 1:
            Event_Participation.objects.filter(scout_id=s, event_id=event_id).delete()
    return HttpResponse('ERROR: Non-AJAX access to dbaccess' )
            

@login_required
def areyougoing(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
#     UserFormSet = modelformset_factory(User, fields=('last_name',))
    
    Event_ParticipationFormSet = inlineformset_factory(Event, Event_Participation, fields=('scout','going',))
    formset = Event_ParticipationFormSet(instance=event)
    
    return render(request, 'events/areyougoing.html', {'event': event, 'form': formset})



# -------
# to do
#     on save, transfer all of request.POST => event
#     save of m2m relationship fails

# add event
# delete event
# bulk-add event_participation of many scouts
# detail-edit event_participation of a single scout

# m2m relationships
#     *** uniqueness
#     create
#     read
#     update
#     delete

# names of event_participants

