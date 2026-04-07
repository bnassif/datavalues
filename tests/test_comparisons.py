import pytest
from datavalues import *

@pytest.mark.parametrize("higher,lower", [
    # Metric bits (×1000)
    (KiloBit, Bit),
    (MegaBit, KiloBit),
    (GigaBit, MegaBit),
    (TeraBit, GigaBit),
    (PetaBit, TeraBit),
    (ExaBit, PetaBit),
    (ZettaBit, ExaBit),
    (YottaBit, ZettaBit),
    (RonnaBit, YottaBit),
    (QuettaBit, RonnaBit),
    # Metric bytes (×1000)
    (KiloByte, Byte),
    (MegaByte, KiloByte),
    (GigaByte, MegaByte),
    (TeraByte, GigaByte),
    (PetaByte, TeraByte),
    (ExaByte, PetaByte),
    (ZettaByte, ExaByte),
    (YottaByte, ZettaByte),
    (RonnaByte, YottaByte),
    (QuettaByte, RonnaByte),
    # Binary bits (×1024)
    (KibiBit, Bit),
    (MebiBit, KibiBit),
    (GibiBit, MebiBit),
    (TebiBit, GibiBit),
    (PebiBit, TebiBit),
    (ExbiBit, PebiBit),
    (ZebiBit, ExbiBit),
    (YobiBit, ZebiBit),
    (RobiBit, YobiBit),
    (QuebiBit, RobiBit),
    # Binary bytes (×1024)
    (KibiByte, Byte),
    (MebiByte, KibiByte),
    (GibiByte, MebiByte),
    (TebiByte, GibiByte),
    (PebiByte, TebiByte),
    (ExbiByte, PebiByte),
    (ZebiByte, ExbiByte),
    (YobiByte, ZebiByte),
    (RobiByte, YobiByte),
    (QuebiByte, RobiByte),
])
def test_comparisons(higher, lower):
    assert higher(1) > lower(1)
    assert higher(1) >= lower(1)
    assert higher(1) >= higher(1)
    assert higher(1) == higher(1)
    assert higher(1) <= higher(1)
    assert lower(1) <= higher(1)
    assert lower(1) >= lower(1)
    assert lower(1) == lower(1)
    assert lower(1) <= lower(1)
    assert lower(1) < higher(1)
