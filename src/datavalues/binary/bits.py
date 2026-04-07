from datavalues.binary.base import BinaryBitClass
from datavalues.base.unit import Bit

from datavalues.registry import register_unit

__all__ = [
    'Bit',
    'KibiBit',
    'MebiBit',
    'GibiBit',
    'TebiBit',
    'PebiBit',
    'ExbiBit',
    'ZebiBit',
    'YobiBit',
    'RobiBit',
    'QuebiBit',
]

@register_unit()
class KibiBit(BinaryBitClass):
    _unit_name = 'Kib'
    _unit_factor = 10

@register_unit()
class MebiBit(BinaryBitClass):
    _unit_name = 'Mib'
    _unit_factor = 20

@register_unit()
class GibiBit(BinaryBitClass):
    _unit_name = 'Gib'
    _unit_factor = 30

@register_unit()
class TebiBit(BinaryBitClass):
    _unit_name = 'Tib'
    _unit_factor = 40

@register_unit()
class PebiBit(BinaryBitClass):
    _unit_name = 'Pib'
    _unit_factor = 50

@register_unit()
class ExbiBit(BinaryBitClass):
    _unit_name = 'Eib'
    _unit_factor = 60

@register_unit()
class ZebiBit(BinaryBitClass):
    _unit_name = 'Zib'
    _unit_factor = 70

@register_unit()
class YobiBit(BinaryBitClass):
    _unit_name = 'Yib'
    _unit_factor = 80

@register_unit()
class RobiBit(BinaryBitClass):
    _unit_name = 'Rib'
    _unit_factor = 90

@register_unit()
class QuebiBit(BinaryBitClass):
    _unit_name = 'Qib'
    _unit_factor = 100
