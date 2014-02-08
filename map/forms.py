'''
Created on Dec 21, 2013
'''
from django.forms.forms import Form
from django.forms.fields import FileField, CharField, IntegerField
from django.forms.util import ErrorList

class MapForm(Form):
    # set file limit to 5MB
    FILE_LIMIT = 5242880
    
    fileName = FileField()
    mapName = CharField(max_length=50, min_length=1)
    mapType = CharField(max_length=50, min_length=1, required=False)
    
    def is_valid(self):
        valid = super(MapForm, self).is_valid()
        
        if valid:
            content = self.cleaned_data['fileName'].read()
            if len(content) > self.FILE_LIMIT:
                self.errors['fileName'] = ErrorList['File size is larger then allowed limit']
                valid = False
            else:
                self.cleaned_data['content'] = content
                self.cleaned_data['filename'] = self.cleaned_data['fileName'].name
                try:
                    self.cleaned_data['extension'] = self.cleaned_data['fileName'].name.split('.')[-1]
                except IndexError:
                    self.cleaned_data['extension']
        
        return valid


class UserMapForm(Form):
    name = CharField(max_length=50, min_length=1)
    svgContent = CharField(min_length=1)
    mapId = IntegerField(min_value=1)