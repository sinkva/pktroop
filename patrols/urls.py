from django.conf.urls import url

from . import views

app_name = 'patrols'

urlpatterns = [
    # ex: /patrols/
    url(r'^$', views.index, name='index'),
    
    # ex: /patrols/dump_all_data/
    url(r'^dump_all_data/$', views.dump_all_data, name='dump_all_data'),

    # ex: /patrols/125/
    url(r'^(?P<patrol_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /patrols/125/update
    url(r'^(?P<patrol_id>[0-9]+)/update/$', views.update, name='update'),

    # ex: /patrols/125/updatesave
    url(r'^(?P<patrol_id>[0-9]+)/updatesave/$', views.updatesave, name='updatesave'),
]
