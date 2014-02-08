from django.views.generic.base import View
from django.http.response import HttpResponse, HttpResponseRedirect,\
    HttpResponseForbidden
from map.forms import MapForm, UserMapForm
from lib.utils import MediaFileUtils, FileUtils, JSONUtils, RequestUtils
from map.models import Map, UserMap
from django.shortcuts import get_object_or_404
from map.exceptions import UserException
from lib.svg import SVG

class MapsView(View):
    
    # TODO: add authentication
    def get(self, request):
        maps = Map.objects.filter(user=request.user)
        response = [current.as_json() for current in maps]
        return HttpResponse(JSONUtils.to_json(response), content_type='application/json')

class MapView(View):
    
    # TODO: get authentication
    def get(self, request):
        params = RequestUtils.get_parameters(request)
        edit_map = get_object_or_404(Map, pk=params['mapId'])
        return HttpResponse(JSONUtils.to_json(edit_map.as_json()), content_type='application/json')
    
    # TODO: get authentication
    def post(self, request):
        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.cleaned_data['content']
            path = MediaFileUtils.get_media_map_path(request.user.username, content, 
                                                 form.cleaned_data['extension'])
            FileUtils.write(path, content)
            new_map = Map(user=request.user, name=form.cleaned_data['mapName'],
                      map_type=form.cleaned_data['mapType'], path=path)
            new_map.save()
            return HttpResponseRedirect('/#/list'.format(new_map.id))
        else:
            print(form.errors)
            return HttpResponse('error during post')
        
        
class UserMapView(View):
    
    # TODO: get authentication
    def get(self, request):
        return HttpResponse('user map get request')
    
    # TODO: get authentication
    def post(self, request):
        data = RequestUtils.get_parameters(request)
        form = UserMapForm(data)
        if form.is_valid():
            original_map = Map.objects.get_id(form.cleaned_data['mapId'])
            if original_map.user != request.user:
                raise UserException('User can\'t edit this map')
            path = MediaFileUtils.get_media_user_map_path(request.user.username, 
                                                          form.cleaned_data['svgContent'],
                                                          FileUtils.get_extension(original_map.path)
                                                          )
            FileUtils.write(path, form.cleaned_data['svgContent'])
            png_path = MediaFileUtils.get_media_map_png(path)
            png_thumbnail_path = MediaFileUtils.get_media_map_png_thumbnail(path)
            svg = SVG(path)
            svg.convert(png_path, 1600)
            svg.convert(png_thumbnail_path, 800)
            UserMap.objects.create_user_map(original_map, 
                                            form.cleaned_data['name'], 
                                            path,
                                            png_path,
                                            png_thumbnail_path)
            return HttpResponse(status=201)
        else:
            return HttpResponseForbidden('error')