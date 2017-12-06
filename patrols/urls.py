from django.conf.urls import url

from . import views

app_name = 'patrols'

urlpatterns = [
    # ex: /patrols/
    url(r'^$', views.index, name='index'),
    
    # ex: /patrols/125/
    url(r'^(?P<patrol_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /patrols/125/update
    url(r'^(?P<patrol_id>[0-9]+)/update/$', views.update, name='update'),

    # ex: /patrols/125/updatesave
    url(r'^(?P<patrol_id>[0-9]+)/updatesave/$', views.updatesave, name='updatesave'),
]
