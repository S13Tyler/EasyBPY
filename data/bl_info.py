
from dataclasses import dataclass

addon_name : str = ""

@dataclass
class BL_Info():
    ''' '''
    name : str
    description : str
    author : str
    version : str
    blender : str
    location : str
    warning : str
    wiki_url : str
    category : str

    def __init__(self, bl_info : dict|None = None):
        if bl_info:
            self.name = bl_info.get('name')
            self.description = bl_info.get('description')
            self.author = bl_info.get('author')
            self.version = bl_info.get('version')
            self.blender = bl_info.get('blender')
            self.location = bl_info.get('location')
            self.warning = bl_info.get('warning')
            self.wiki_url = bl_info.get('wiki_url')
            self.category = bl_info.get('category')
