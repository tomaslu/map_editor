'''
Created on Dec 12, 2013

@author: luka
'''
import json
import os
import hashlib
from map_editor.settings import MEDIA_DIR

class RequestUtils(object):
    
    @classmethod
    def get_parameters(cls, request):
        data = None
        
        if request.method=='GET':
            data = request.GET
        elif request.method=='POST':
            if request.POST:
                data = request.POST
            elif request.body:
                data = JSONUtils.from_json(request.body)
        elif request.method=='PUT':
            pass
        elif request.method=='DELETE':
            pass
        
        return data
    
    
class JSONUtils(object):
    
    @classmethod
    def to_json(cls, value):
        '''
        Converts obj to JSON.
        
        @param value: obj
        
        @return: string
        '''
        return json.dumps(value)
    
    @classmethod
    def from_json(cls, value):
        '''
        Converts string to obj.
        
        @param value: string
        
        @return: obj
        '''
        return json.loads(value)
    
    
class FileUtils(object):
    
    @classmethod
    def write(cls, path, content):
        with open(path, 'wb') as f:
            f.write(content)
            
    @classmethod
    def get_extension(cls, path):
        return os.path.splitext(path)[1].strip('.')


class MediaFileUtils(FileUtils):
    
    @classmethod
    def get_media_filename(cls, user, content, extension):
        '''
        Returns media filename that is md5 hash of user information and file
        content.
        
        @param user: username
        @param content: file content
        @param extension: file extension
        
        @return: file name
        '''
        md5_hash = hashlib.md5()
        md5_hash.update(user)
        md5_hash.update(content)
        filename = '.'.join((md5_hash.hexdigest(), extension))
        return filename
    
    @classmethod
    def get_media_map_path(cls, user, content, extension):
        '''
        Returns media file path for maps.
        
        @param user: username
        @param content: file content
        @param extension: file extension
        
        @return: file path
        '''
        filename = cls.get_media_filename(user, content, extension)
        return os.path.join(MEDIA_DIR, 'map', filename)
    
    @classmethod
    def get_media_user_map_path(cls, user, content, extension):
        '''
        Returns media file path for user maps.
        
        @param user: username
        @param content: file content
        @param extension: file extension
        
        @return: file path
        '''
        filename = cls.get_media_filename(user, content, extension)
        return os.path.join(MEDIA_DIR, 'user_map', filename)
    
    @classmethod
    def get_media_map_png(cls, original_path):
        return original_path.replace('svg', 'png')
    
    @classmethod
    def get_media_map_png_thumbnail(cls, original_path):
        (filename, _) = os.path.splitext(original_path)
        return '{}_thumbnail.png'.format(filename)
