
from enum import Enum
from typing import Any


class EasyEnum(Enum):
    '''
    '''
    @classmethod
    def from_value(cls,
                   value : Any|None = None
                   ):
        for i in cls:
            if value == i.value: # passed value is member value
                return i
            if isinstance(value, str): # passed value is string and equals member name
                if value.upper() == i.name:
                    return i

    @classmethod
    def get_names(cls):
        return cls._member_names_

    @classmethod
    def get_dict(cls):
        return {member.name : member.value for member in cls}


class EObjectType(EasyEnum):
    ALL      = [('all',      'ALL',      'Bl_Object_Type: ALL')]
    MESH     = [('mesh',     'MESH',     'Bl_Object_Type: MESH')]
    CURVE    = [('curve',    'CURVE',    'Bl_Object_Type: CURVE')]
    SURFACE  = [('surface',  'SURFACE',  'Bl_Object_Type: SURFACE')]
    META     = [('meta',     'META',     'Bl_Object_Type: META')]
    FONT     = [('font',     'FONT',     'Bl_Object_Type: FONT')]
    ARMATURE = [('armature', 'ARMATURE', 'Bl_Object_Type: ARMATURE')]
    LATTICE  = [('lattice',  'LATTICE',  'Bl_Object_Type: LATTICE')]
    EMPTY    = [('empty',    'EMPTY',    'Bl_Object_Type: EMPTY')]
    CAMERA   = [('camera',   'CAMERA',   'Bl_Object_Type: CAMERA')]
    LIGHT    = [('light',    'LIGHT',    'Bl_Object_Type: LIGHT')]
    SPEAKER  = [('speaker',  'SPEAKER',  'Bl_Object_Type: SPEAKER')]

    @classmethod
    def from_value(cls, value : str|None = None):
        for member in cls:
            if value in member.value[0]:
                return member

    def value_lower(self):
        return self.value[0][0]


class ECaseRule(EasyEnum):
    '''
    '''
    DEFAULT     = [('default',    'Default',    'Do not modify.')]
    LOWER       = [('lower',      'lowercase',  'Set all letters to lowercase. (ex: _objectname)')]
    UPPER       = [('upper',      'UPPERCASE',  'Set all letters to uppercase. (ex: _OBJECTNAME)')]
    CAMELCASE   = [('camelcase',  'camelCase',  'Use camelcase conventions. (ex: _objectName)')]
    PASCALCASE  = [('pascalcase', 'PascalCase', 'Use pascalcase conventions. (ex: _ObjectName)')]

    def value_lower(self):
        return self.value[0][0]
