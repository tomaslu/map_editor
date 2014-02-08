'''
Created on Dec 11, 2013
'''
from django.conf.urls import patterns, url
from authentication.views import RegisterView, LoginView, logout_user,\
    authenticated_page

urlpatterns = patterns('',
                       url(r'^register$', RegisterView.as_view(), name='authentication_register'),
                       url(r'^login$', LoginView.as_view(), name='authentication_login'),
                       url(r'^logout_user$', logout_user, name='authentication_logout_user'),
                       url(r'^authenticated_page$', authenticated_page, name='authentication_authenticated_page'),
                       )