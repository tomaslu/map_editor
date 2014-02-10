'''
Created on Jan 5, 2014
'''
from lxml import etree
import subprocess

class SVG(object):
    
    def __init__(self, svg_path):
        self.svg_path = svg_path
        with open(self.svg_path, 'r') as f:
            content = f.read()
        try:
            self.tree = etree.fromstring(content)
            self.width = int(float(self.tree.get('width')))
            self.height = int(float(self.tree.get('height')))
        except Exception as e:
            print(e)
        
    def convert(self, new_file, width, height=None):
        if not height:
            height = self.height*width/self.width
        subprocess.call(['inkscape', '-z', '-e', new_file, 
                         '-w {}'.format(width), '-h {}'.format(height), 
                         self.svg_path])
        