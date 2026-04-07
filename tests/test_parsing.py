import pytest
from datavalues import *

@pytest.mark.parametrize('obj_class', [
    (Bit),
    (KiloBit),
    (KibiBit),
    (MegaBit),
    (MebiBit),
    (GigaBit),
    (GibiBit),
    (TeraBit),
    (TebiBit),
    (PetaBit),
    (PebiBit),
    (ExaBit),
    (ExbiBit),
    (ZettaBit),
    (ZebiBit),
    (YottaBit),
    (YobiBit),
    (RonnaBit),
    (RobiBit),
    (Byte),
    (KiloByte),
    (KibiByte),
    (MegaByte),
    (MebiByte),
    (GigaByte),
    (GibiByte),
    (TeraByte),
    (TebiByte),
    (PetaByte),
    (PebiByte),
    (ExaByte),
    (ExbiByte),
    (ZettaByte),
    (ZebiByte),
    (YottaByte),
    (YobiByte),
    (RonnaByte),
    (RobiByte),
])
def test_parsing(obj_class):
    short_name = obj_class._unit_name
    long_name = obj_class.__name__
    # Test getting object by its short name
    assert get_unit(short_name) == obj_class
    # Test getting object by its long name
    assert get_unit(long_name) == obj_class
    # Test getting object by its long name with an 's' appended
    assert get_unit(long_name + 's') == obj_class
    # Test getting object by its long name in lowercase
    assert get_unit(long_name.lower()) == obj_class

    # Test constructing object with short name from string
    assert from_string(f'15 {short_name}') == obj_class(15)
    # Test contruction object with long name from string
    assert from_string(f'15 {long_name}') == obj_class(15)
