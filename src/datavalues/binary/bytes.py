from datavalues.binary.base import BinaryByteClass
from datavalues.base.unit import Byte

from datavalues.registry import register_unit

__all__ = [
    'Byte',
    'KibiByte',
    'MebiByte',
    'GibiByte',
    'TebiByte',
    'PebiByte',
    'ExbiByte',
    'ZebiByte',
    'YobiByte',
    'RobiByte',
    'QuebiByte',
]

@register_unit()
class KibiByte(BinaryByteClass):
    _unit_name = 'KiB'
    _unit_factor = 10

@register_unit()
class MebiByte(BinaryByteClass):
    _unit_name = 'MiB'
    _unit_factor = 20

@register_unit()
class GibiByte(BinaryByteClass):
    _unit_name = 'GiB'
    _unit_factor = 30

@register_unit()
class TebiByte(BinaryByteClass):
    _unit_name = 'TiB'
    _unit_factor = 40

@register_unit()
class PebiByte(BinaryByteClass):
    _unit_name = 'PiB'
    _unit_factor = 50

@register_unit()
class ExbiByte(BinaryByteClass):
    _unit_name = 'EiB'
    _unit_factor = 60

@register_unit()
class ZebiByte(BinaryByteClass):
    _unit_name = 'ZiB'
    _unit_factor = 70

@register_unit()
class YobiByte(BinaryByteClass):
    _unit_name = 'YiB'
    _unit_factor = 80

@register_unit()
class RobiByte(BinaryByteClass):
    _unit_name = 'RiB'
    _unit_factor = 90

@register_unit()
class QuebiByte(BinaryByteClass):
    _unit_name = 'QiB'
    _unit_factor = 100
