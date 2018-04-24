from django.conf.urls import url
# from django.views.generic.list import ListView, DetailView

from . import views

app_name = 'profiles'

urlpatterns = [
    # ex: /profiles/
    url(r'^$', views.index, name='index'),

    # ex: /profiles/dump_all_data/
    url(r'^dump_all_data/$', views.dump_all_data, name='dump_all_data'),

    # ex: /profiles/125/
    url(r'^(?P<Profile_id>[0-9]+)/$', views.detail, name='detail'),
    
    # ex: /profiles/125/update
    url(r'^(?P<Profile_id>[0-9]+)/update/$', views.update, name='update'),

    # ex: /profiles/125/updatesave
    url(r'^(?P<Profile_id>[0-9]+)/updatesave/$', views.updatesave, name='updatesave'),
]
