#!/usr/bin/env python3

from abc import ABCMeta
from functools import wraps

def _format(num: float):
    # Remove decimal from float as its own float trailing 0 (i.e. 0.523)
    decimal = float(f"0.{str(num).split('.')[1]}")
    # Return non-decimal with commas, and rounded decimal appended
    return f"{'{:,}'.format(int(num))}.{str(round(decimal, 2)).split('.')[1]}"

class BaseDataModel(metaclass=ABCMeta):
    _unit_data = {
        'byte': {
            'unit': 'B',
            'conversion_factor': int(f'1{"0" * 0}'),
        },
        'kilobyte': {
            'unit': 'KB',
            'conversion_factor': int(f'1{"0" * 3}'),
        },
        'megabyte': {
            'unit': 'MB',
            'conversion_factor': int(f'1{"0" * 6}'),
        },
        'gigabyte': {
            'unit': 'GB',
            'conversion_factor': int(f'1{"0" * 9}'),
        },
        'terabyte': {
            'unit': 'TB',
            'conversion_factor': int(f'1{"0" * 12}'),
        },
        'petabyte': {
            'unit': 'PB',
            'conversion_factor': int(f'1{"0" * 15}'),
        },
        'exabyte': {
            'unit': 'EB',
            'conversion_factor': int(f'1{"0" * 18}'),
        },
        'zettabyte': {
            'unit': 'ZB',
            'conversion_factor': int(f'1{"0" * 21}'),
        },
        'yottabyte': {
            'unit': 'YB',
            'conversion_factor': int(f'1{"0" * 24}'),
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
                        isinstance(other, float) or
                        isinstance(other, self.__class__)):
                    raise TypeError
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
        return Byte(self.to_bytes() * other.to_bytes()).convert(self.unit.lower())
    
    @_validate
    def __truediv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value // other)
        return Byte(self.to_bytes() // other.to_bytes()).convert(self.unit.lower())
    
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
        return Byte(self.to_bytes() * other.to_bytes()).convert(self.unit.lower())
    
    @_validate
    def __itruediv__(self, other):
        if (isinstance(other, int) or isinstance(other, float)):
            return self.__class__(self.value // other)
        return Byte(self.to_bytes() // other.to_bytes()).convert(self.unit.lower())

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
        for key, value in self.__class__._unit_data.items():
            if value['unit'].lower() == unit:
                unit = key
        
        try:
            conversion_rate = self._conversion_factor() / self.__class__._unit_data[unit]['conversion_factor']
            dest_class = unit.title().replace('b','B')
            if dest_class in globals():
                return globals()[dest_class](self.value * conversion_rate)
            else:
                return self.value * conversion_rate
        except KeyError:
            raise ValueError(f"Invalid unit specified ({unit}). Select a valid unit: {self.__class__._units_short} ")

for unit in BaseDataModel._unit_data.keys():
    class_name = unit.title().replace('b','B')
    globals()[class_name] = type(class_name, (BaseDataModel,), {})