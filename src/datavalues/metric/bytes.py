from datavalues.metric.base import MetricByteClass
from datavalues.base.unit import Byte

from datavalues.registry import register_unit

__all__ = [
    'Byte',
    'KiloByte',
    'MegaByte',
    'GigaByte',
    'TeraByte',
    'PetaByte',
    'ExaByte',
    'ZettaByte',
    'YottaByte',
    'RonnaByte',
    'QuettaByte',
]

@register_unit()
class KiloByte(MetricByteClass):
    _unit_name = 'KB'
    _unit_factor = 1

@register_unit()
class MegaByte(MetricByteClass):
    _unit_name = 'MB'
    _unit_factor = 2

@register_unit()
class GigaByte(MetricByteClass):
    _unit_name = 'GB'
    _unit_factor = 3

@register_unit()
class TeraByte(MetricByteClass):
    _unit_name = 'TB'
    _unit_factor = 4

@register_unit()
class PetaByte(MetricByteClass):
    _unit_name = 'PB'
    _unit_factor = 5

@register_unit()
class ExaByte(MetricByteClass):
    _unit_name = 'EB'
    _unit_factor = 6

@register_unit()
class ZettaByte(MetricByteClass):
    _unit_name = 'ZB'
    _unit_factor = 7

@register_unit()
class YottaByte(MetricByteClass):
    _unit_name = 'YB'
    _unit_factor = 8

@register_unit()
class RonnaByte(MetricByteClass):
    _unit_name = 'RB'
    _unit_factor = 9

@register_unit()
class QuettaByte(MetricByteClass):
    _unit_name = 'QB'
    _unit_factor = 10
