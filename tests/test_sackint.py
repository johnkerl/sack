import pytest
from sack import sackint

def test_gcd():
    assert sackint.gcd(0, 0) == 0
    assert sackint.gcd(0, 1) == 1
    assert sackint.gcd(1, 0) == 1
    assert sackint.gcd(1, 2) == 1

    assert sackint.gcd(4, 5) == 1
    assert sackint.gcd(4, 6) == 2

    assert sackint.gcd(1296,1728) == 432
    # test numbers over 2^32

    assert sackint.gcd(0, -1) == 1
    assert sackint.gcd(-1, 0) == 1
    assert sackint.gcd(1, -2) == 1
    assert sackint.gcd(-1, 2) == 1

    assert sackint.gcd(-4, 6) == 2
    assert sackint.gcd(4, -6) == 2
    assert sackint.gcd(-4, -6) == 2


# def gcd(a, b):
# def extgcd(a, b):
# def eulerphi(n, cached_n_and_phi=[2,1]):
# def intexp(x, e):
# def intmodexp(x, e, m):
# def intmodrecip(x, m):
# def factorial(n):
# def num_ptnsm(n, m):
# def num_ptns(n):
# def ptnsm(n, m):
# def ptns(n):
