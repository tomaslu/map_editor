from django.contrib import admin
from map.models import Map, UserMap

# Register your models here.

class MapAdmin(admin.ModelAdmin):
    fields = ['user', 'name', 'map_type', 'time_created']
    
class UserMapAdmin(admin.ModelAdmin):
    fields = ['original_map', 'name', 'time_created']
    
admin.site.register(Map, MapAdmin)
admin.site.register(UserMap, UserMapAdmin)
