from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from map.exceptions import MapException

# managers
class MapManager(models.Manager):
    
    @classmethod
    def get_id(cls, map_id):
        '''
        Returns Map object based on given map_id.
        
        @param map_id: int
        @return: Map
        @raise MapException: if Map does not exist
        '''
        try:
            return Map.objects.get(id=map_id)
        except Map.DoesNotExist:
            raise MapException('Map does not exist')


class UserMapManager(models.Manager):
    
    @classmethod
    def create_user_map(cls, original_map, name, path, png, png_thumbnail):
        '''
        Creates new user map.
        '''
        user_map = UserMap(original_map=original_map, name=name, path=path,
                           png=png, png_thumbnail=png_thumbnail)
        user_map.save()
        return user_map

# Create your models here.

class Map(models.Model):
    '''
    Base model for working with maps (represents original maps; before editing).
    '''
    WORLD = 'world'
    CONTINENT = 'continent'
    COUNTRY = 'country'
    STATE = 'state'
    COUNTY = 'country'
        
    MAP_TYPES = ((WORLD, WORLD.capitalize()), (CONTINENT, CONTINENT.capitalize()), 
                 (COUNTRY, COUNTRY.capitalize()), (STATE, STATE.capitalize()),
                 (COUNTY, COUNTY.capitalize()))
        
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    map_type = models.CharField(max_length=50, choices=MAP_TYPES)
    time_created = models.DateTimeField(default=datetime.now())
    path = models.FilePathField()
    
    objects = MapManager()
    
    def as_json(self):
        return {'id': self.id, 'name': self.name, 'map_type': self.map_type,
                'url': self.url, 'time_created': str(self.time_created),
                'user_maps': [user_map.as_json() for user_map in self.user_maps]}
    
    def _get_url(self):
        return self.path[len(settings.BASE_DIR+'/app'):]
    
    def _get_user_maps(self):
        return UserMap.objects.filter(original_map=self)
    
    url = property(_get_url)
    user_maps = property(_get_user_maps)
        
    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.user)
    
    
class UserMap(models.Model):
    '''
    Model for working with user maps (maps after editing).
    '''
    original_map = models.ForeignKey(Map)
    name = models.CharField(max_length=50)
    time_created = models.DateTimeField(default=datetime.now())
    path = models.FilePathField()
    png = models.FilePathField()
    png_thumbnail = models.FilePathField()
    
    objects = UserMapManager()
    
    def get_png_url(self):
        return self.png[len(settings.BASE_DIR+'/app'):]
    
    def get_png_thumbnail_url(self):
        return self.png_thumbnail[len(settings.BASE_DIR+'/app'):]
    
    def as_json(self):
        return {'id': self.id, 'name': self.name, 
                'time_created': str(self.time_created), 'path': self.path,
                'png_url': self.get_png_url(), 
                'png_thumbnail_url': self.get_png_thumbnail_url()}
    
    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.original_map)
