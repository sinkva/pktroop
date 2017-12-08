from django.conf.urls import url
# from django.views.generic.list import ListView, DetailView

from . import views

app_name = 'profiles'

urlpatterns = [
    # ex: /profiles/
    url(r'^$', views.index, name='index'),

    # ex: /profiles/125/

    url(r'^(?P<Profile_id>[0-9]+)/$', views.detail, name='detail'),
    
    # ex: /profiles/125/update
    url(r'^(?P<Profile_id>[0-9]+)/update/$', views.update, name='update'),

    # ex: /profiles/125/updatesave
    url(r'^(?P<Profile_id>[0-9]+)/updatesave/$', views.updatesave, name='updatesave'),
]
