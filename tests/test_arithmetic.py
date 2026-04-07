import pytest
from datavalues import *

@pytest.mark.parametrize("unit", [
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
def test_arithmetic(unit):
    # Test Substraction
    assert unit(10) - unit(5) == 5
    # Test addition
    assert unit(5) + unit(5) == 10
    # Test Division
    assert unit(10) / unit(2) == 5.0
    # Test addition
    assert unit(10) + unit(5) == 15.0
    
    # Test division is float and ratio
    result = unit(99) / unit(41)
    assert isinstance(result, float)
    assert result == pytest.approx(99 / 41, rel=1e-12, abs=0.0)
    
    # Test multiplication
    assert unit(10) * 10 == unit(100)
    # Test multiplcation error
    with pytest.raises(TypeError):
        _ = unit(2) * unit(5)
    
    # Test in-place operations    
    value = unit(20)
    value += 15
    assert value == 35
    value -= 25
    assert value == 10
    value /= 5
    assert value == 2
    value //= 2
    assert value == 1
    value *= 25
    assert value == 25
