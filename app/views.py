# Create your views here.
from django.shortcuts import render

def home(request):
    map_content = None
    context = {'user': request.user, 'page': 'home', 'map': map_content}
    return render(request, 'partials/home.html', context)

def gallery(request):
    context = {'user': request.user, 'page': 'gallery'}
    return render(request, 'partials/gallery.html', context)

def about(request):
    context = {'user': request.user, 'page': 'about'}
    return render(request, 'partials/about.html', context)

def upload(request):
    context = {'user': request.user, 'page': 'upload'}
    return render(request, 'partials/about.html', context)

