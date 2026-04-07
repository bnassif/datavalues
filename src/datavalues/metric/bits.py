from datavalues.metric.base import MetricBitClass
from datavalues.base.unit import Bit

from datavalues.registry import register_unit

__all__ = [
    'Bit',
    'KiloBit',
    'MegaBit',
    'GigaBit',
    'TeraBit',
    'PetaBit',
    'ExaBit',
    'ZettaBit',
    'YottaBit',
    'RonnaBit',
    'QuettaBit',
]

@register_unit()
class KiloBit(MetricBitClass):
    _unit_name = 'Kb'
    _unit_factor = 1

@register_unit()
class MegaBit(MetricBitClass):
    _unit_name = 'Mb'
    _unit_factor = 2

@register_unit()
class GigaBit(MetricBitClass):
    _unit_name = 'Gb'
    _unit_factor = 3

@register_unit()
class TeraBit(MetricBitClass):
    _unit_name = 'Tb'
    _unit_factor = 4

@register_unit()
class PetaBit(MetricBitClass):
    _unit_name = 'Pb'
    _unit_factor = 5

@register_unit()
class ExaBit(MetricBitClass):
    _unit_name = 'Eb'
    _unit_factor = 6

@register_unit()
class ZettaBit(MetricBitClass):
    _unit_name = 'Zb'
    _unit_factor = 7

@register_unit()
class YottaBit(MetricBitClass):
    _unit_name = 'Yb'
    _unit_factor = 8

@register_unit()
class RonnaBit(MetricBitClass):
    _unit_name = 'Rb'
    _unit_factor = 9

@register_unit()
class QuettaBit(MetricBitClass):
    _unit_name = 'Qb'
    _unit_factor = 10
