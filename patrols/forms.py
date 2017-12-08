from django.forms import ModelForm
from django.forms.models import modelform_factory

class PatrolForm(ModelForm):
    class Meta:
        model = Patrol
        fields = '__all__'
