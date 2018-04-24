from django.conf.urls import url

from . import views

app_name = 'events'

urlpatterns = [
    # ex: /events/
    url(r'^$', views.index, name='index'),

    # ex: /events/dump_all_data/
    url(r'^dump_all_data/$', views.dump_all_data, name='dump_all_data'),

    # ex: /events/125/
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /events/125/update
    url(r'^(?P<event_id>[0-9]+)/update/$', views.update, name='update'),

    # ex: /events/125/updatesave
    url(r'^(?P<event_id>[0-9]+)/updatesave/$', views.updatesave, name='updatesave'),

    # ex: /events/125/dbaccess/
    url(r'^(?P<event_id>[0-9]+)/dbaccess/$', views.dbaccess, name='dbaccess'),

    # ex: /events/125/areyougoing/
    url(r'^(?P<event_id>[0-9]+)/areyougoing/$', views.areyougoing, name='areyougoing'),

    # ex: /events/125/participationsave
    url(r'^(?P<event_id>[0-9]+)/participationsave/$', views.participationsave, name='participationsave'),

]
