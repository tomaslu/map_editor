'''
Created on Dec 21, 2013
'''
from django.conf.urls import patterns, url
from map.views import MapView, MapsView, UserMapView

urlpatterns = patterns('',
                       url('^$', MapsView.as_view(), name='map_maps'),
                       url('^map/(?P<mapId>\d+)/$', MapView.as_view(), name='map_map'),
                       url('^map/$', MapView.as_view(), name='map_map'),
                       url('^user_map/(?P<mapId>\d+)/$', UserMapView.as_view(), name='map_map'),
                       url('^user_map$', UserMapView.as_view(), name='map_map'),
                       )