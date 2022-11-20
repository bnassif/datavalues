#!/usr/bin/env python3

from abc import ABCMeta
from functools import wraps

def _format(num: float):
    try:
        # Remove decimal from float as its own float trailing 0 (i.e. 0.523)
        decimal = float(f"0.{str(num).split('.')[1]}")
        # Return non-decimal with commas, and rounded decimal appended
        return f"{'{:,}'.format(int(num))}.{str(round(decimal, 2)).split('.')[1]}"
    except IndexError:
        return f"{'{:,}'.format(int(num))}"

class BaseDataModel(metaclass=ABCMeta):
    _unit_data = {
        'byte': {
            'unit': 'B',
            'conversion_factor': int(f'1{"000" * 0}'),
        },
        'kilobyte': {
            'unit': 'KB',
            'conversion_factor': int(f'1{"000" * 1}'),
        },
        'megabyte': {
            'unit': 'MB',
            'conversion_factor': int(f'1{"000" * 2}'),
        },
        'gigabyte': {
            'unit': 'GB',
            'conversion_factor': int(f'1{"000" * 3}'),
        },
        'terabyte': {
            'unit': 'TB',
            'conversion_factor': int(f'1{"000" * 4}'),
        },
        'petabyte': {
            'unit': 'PB',
            'conversion_factor': int(f'1{"000" * 5}'),
        },
        'exabyte': {
            'unit': 'EB',
            'conversion_factor': int(f'1{"000" * 6}'),
        },
        'zettabyte': {
            'unit': 'ZB',
            'conversion_factor': int(f'1{"000" * 7}'),
        },
        'yottabyte': {
            'unit': 'YB',
            'conversion_factor': int(f'1{"000" * 8}'),
        },
    }
    _units_long = [key for key in _unit_data.keys()]
    _units_short = [value['unit'].lower() for value in _unit_data.values()]
    
    #unit = _unit_data[__name__.lower()]

    def __init__(self, value: float, bits: bool = False):
        self.formatted = True
        self.value = value / 8 if bits else value
        
        self.unit = self.__class__._unit_data[self.__class__.__name__.lower()]['unit']
        self.conversion_factor = self.__class__._unit_data[self.__class__.__name__.lower()]['conversion_factor']

    def _validate(func):
        @wraps(func)
        def wrapper(self, other):
            if type(other).__name__ not in globals():
                if not (isinstance(other, int) or
                        issubclass(other, int) or # Allow subclasses for third-party compatibility
                        isinstance(other, float) or
                        issubclass(other, float) or # Allow subclasses for third-party compatibility
                        issubclass(other.__class__, BaseDataModel)):
                    raise TypeError('Must either pass a float/int or an object from data.data')
            return func(self, other)
        return wrapper

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    def __str__(self):
        if self.formatted:
            return f'{_format(self.value)} {self.unit}'
        return f'{self.value} {self.unit}'
    
    def to_bytes(self):
        return self.convert('byte').value

    @_validate
    def __add__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value + other)
        return Byte(self.to_bytes() + other.to_bytes()).convert(self.unit.lower())

    @_validate
    def __sub__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value - other)
        return Byte(self.to_bytes() - other.to_bytes()).convert(self.unit.lower())
    
    @_validate
    def __mul__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value * other)
        raise TypeError('Cannot multiply data objects')
    
    @_validate
    def __truediv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value / other)
        return self.to_bytes() / other.to_bytes()
    
    @_validate
    def __floordiv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value // other)
        return self.to_bytes() // other.to_bytes()
    
    @_validate
    def __iadd__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value + other)
        return Byte(self.to_bytes() + other.to_bytes()).convert(self.unit.lower())

    @_validate
    def __isub__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value - other)
        return Byte(self.to_bytes() - other.to_bytes()).convert(self.unit.lower())
    
    @_validate
    def __imul__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value * other)
        raise TypeError('Cannot multiply data objects')
    
    @_validate
    def __itruediv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value / other)
        return self.to_bytes() / other.to_bytes()
    
    @_validate
    def __ifloordiv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value // other)
        return self.to_bytes() // other.to_bytes()

    @_validate
    def __eq__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.value == other
        return self.to_bytes() == other.to_bytes()
    
    @_validate
    def __lt__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.value < other
        return self.to_bytes() < other.to_bytes()

    @_validate
    def __gt__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.value > other
        return self.to_bytes() > other.to_bytes()
    
    @_validate
    def __le__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.value <= other
        return self.to_bytes() <= other.to_bytes()

    @_validate
    def __ge__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.value >= other
        return self.to_bytes() >= other.to_bytes()

    def _conversion_factor(self):
        return self.__class__._unit_data[self.__class__.__name__.lower()]['conversion_factor']

    def convert(self, unit):
        # Return top-level unit name if abbreviated name was supplied
        if unit.lower() in self.__class__._unit_data:
            unit = unit.lower()
        else:
            unit = dict((value['unit'].lower(), key) for key, value in self.__class__._unit_data.items()).get(unit.lower())
        try:
            dest_class = unit.title().replace('b','B')
            if dest_class in globals():
                return globals()[dest_class](self.value * self._conversion_factor() / self.__class__._unit_data[unit]['conversion_factor'])
            else:
                raise RuntimeError(f'You must import data.data.{dest_class} to convert to {unit}.')
        except KeyError:
            raise ValueError(f"Invalid unit specified ({unit}). Select a valid unit: {self.__class__._units_short} ")

class Byte(BaseDataModel):
    ...
class KiloByte(BaseDataModel):
    ...
class MegaByte(BaseDataModel):
    ...
class GigaByte(BaseDataModel):
    ...
class TeraByte(BaseDataModel):
    ...
class PetaByte(BaseDataModel):
    ...
class ExaByte(BaseDataModel):
    ...
class ZettaByte(BaseDataModel):
    ...
class YottaByte(BaseDataModel):
    ...
