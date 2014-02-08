'''
Created on Dec 10, 2013

@author: luka
'''
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from app.views import home, gallery, about
from django.http.response import HttpResponse

def upload_file(request):
    return HttpResponse('uploading file...')

urlpatterns = patterns('',
                       url('^$', TemplateView.as_view(template_name='index.html'), name='app_index'),
                       url('^partials/home.html$', home, name='app_home'),
                       url('^partials/gallery.html$', gallery, name='app_gallery'),
                       url('^partials/about.html$', about, name='app_about'),
                       url('^partials/login.html$', TemplateView.as_view(template_name='partials/login.html'), name='app_login'),
                       url('^partials/register.html$', TemplateView.as_view(template_name='partials/register.html'), name='app_register'),
                       url('^partials/upload.html$', TemplateView.as_view(template_name='partials/upload.html'), name='app_upload'),
                       url('^partials/list.html$', TemplateView.as_view(template_name='partials/list.html'), name='app_list'),
                       url('^partials/edit.html$', TemplateView.as_view(template_name='partials/edit.html'), name='app_edit'),
                       )