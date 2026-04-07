from datavalues.base.core import BaseDataClass
from datavalues.registry import register_unit

__all__ = ['Bit', 'Byte']

@register_unit()
class Bit(BaseDataClass):
    _unit_name = 'b'
    _unit_factor = 0
    _is_bits = True

@register_unit()
class Byte(BaseDataClass):
    _unit_name = 'B'
    _unit_factor = 0
