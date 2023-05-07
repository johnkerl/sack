import pytest
from sack import sackint

def test_gcd():
    assert sackint.gcd(4, 6) == 2
