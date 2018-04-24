from django.forms import ModelForm, Textarea, DateInput
from django.forms.models import modelform_factory
from .models import Event, Event_Participation, User
from django.contrib.admin.widgets import AdminDateWidget
from bootstrap_datepicker.widgets import DatePicker

# -------------------------------------------------

class EventDateInput(DateInput):
    input_type = 'date'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'event_name': Textarea(attrs={'cols': 40, 'rows': 1, 'autofocus': 'autofocus'}),
            'start_date': EventDateInput(),
            'end_date': EventDateInput(),
            'full_description': Textarea(attrs={'cols': 40, 'rows': 1}),
            'short_description': Textarea(attrs={'cols': 40, 'rows': 1}),
            'location': Textarea(attrs={'cols': 40, 'rows': 1}), }

        exclude = ('event_participants',)

#     def __init__(self):
#         self.fields['event_name'].widget.attrs.update({'autofocus': 'autofocus'})

# -------------------------------------------------

class Event_ParticipationForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_participants', ]

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import CheckboxSelectMultiple
        
        super(Event_ParticipationForm, self).__init__(*args, **kwargs)
        
        self.fields["event_participants"].widget = CheckboxSelectMultiple()
        self.fields["event_participants"].queryset = User.objects.all()

        

