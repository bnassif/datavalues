from __future__ import annotations

import re
from typing import Dict, Type, TYPE_CHECKING

if TYPE_CHECKING:
    from datavalues.base.core import BaseDataClass

__all__ = [
    'get_unit',
    'from_string',
]

_PATTERN = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*([A-Za-z]+)\s*$")

_UNIT_REGISTRY: Dict[str, BaseDataClass] = {}
_UNIT_NAME_REGISTRY: Dict[str, BaseDataClass] = {}

def register_unit():
    def deco(cls: Type[BaseDataClass]):
        full_name = cls.__name__
        abrev_name = cls._unit_name
        
        _UNIT_REGISTRY[full_name.title()] = cls
        _UNIT_NAME_REGISTRY[abrev_name] = cls
        return cls
    return deco

def get_unit(name: str):
    name = name.rstrip('s')
    if len(name) <= 3 and name.title() != 'Bit':
        return _UNIT_NAME_REGISTRY[name]
    return _UNIT_REGISTRY[name.title()]

def from_string(string):
    match = _PATTERN.match(string)
    
    value = match.group(1)
    if '.' in value:
        value = float(value)
    else:
        value = int(value)
    unit = match.group(2)
    
    unit_class: Type = get_unit(unit)
    return unit_class(value)
