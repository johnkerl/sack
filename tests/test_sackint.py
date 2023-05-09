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
    assert sackint.gcd(18446744073709551615, 13715753599) == 6700417
    assert sackint.gcd(13715753599, 18446744073709551615) == 6700417

    assert sackint.gcd(0, -1) == 1
    assert sackint.gcd(-1, 0) == 1
    assert sackint.gcd(1, -2) == 1
    assert sackint.gcd(-1, 2) == 1

    assert sackint.gcd(-4, 6) == 2
    assert sackint.gcd(4, -6) == 2
    assert sackint.gcd(-4, -6) == 2


def test_extgcd():

    assert sackint.extgcd(0,1) == [1, 0, 1]
    assert sackint.extgcd(1,1) == [1, 0, 1]
    assert sackint.extgcd(1,2) == [1, 1, 0]

    assert sackint.extgcd(4,6) == [2, -1, 1]

    assert sackint.extgcd(1296,1728) == [432, -1, 1]
    assert sackint.extgcd(1728,1296) == [432, 1, -1]

    assert sackint.extgcd(18446744073709551615, 13715753599) == [6700417, -99, 133148182498]
    assert sackint.extgcd(13715753599, 18446744073709551615) == [6700417, 133148182498, -99]

def test_eulerphi():
    assert sackint.eulerphi(0) == 0
    assert sackint.eulerphi(1) == 0
    assert sackint.eulerphi(2) == 1
    assert sackint.eulerphi(3) == 2
    assert sackint.eulerphi(4) == 2
    assert sackint.eulerphi(5) == 4
    assert sackint.eulerphi(6) == 2
    assert sackint.eulerphi(8) == 4
    assert sackint.eulerphi(10) == 4
    assert sackint.eulerphi(100) == 40
    assert sackint.eulerphi(101) == 100
    assert sackint.eulerphi(1000) == 400
    assert sackint.eulerphi(1001) == 720

def test_intexp():
    assert sackint.intexp(0, 0) == 1

    assert sackint.intexp(0, 1) == 0
    assert sackint.intexp(0, 3) == 0

    assert sackint.intexp(1, 0) == 1
    assert sackint.intexp(2, 0) == 1
    assert sackint.intexp(3, 0) == 1

    assert sackint.intexp(7, 5) == 16807

def test_intmodexp():
    assert sackint.intmodexp(1, 0, 11) == 1
    assert sackint.intmodexp(1, 1, 11) == 1
    assert sackint.intmodexp(1, -2, 11) == 1

    assert sackint.intmodexp(2, 0, 11) == 1
    assert sackint.intmodexp(2, 1, 11) == 2
    assert sackint.intmodexp(2, -1, 11) == 6
    assert sackint.intmodexp(2, -2, 11) == 3
    assert sackint.intmodexp(2, 5, 11) == 10
    assert sackint.intmodexp(2, 9, 11) == 6
    assert sackint.intmodexp(2, 10, 11) == 1

    assert sackint.intmodexp(2, 0, 12) == 1
    assert sackint.intmodexp(2, 1, 12) == 2
    assert sackint.intmodexp(2, 10, 12) == 4

    assert sackint.intmodexp(3, 0, 11) == 1
    assert sackint.intmodexp(3, 1, 11) == 3
    assert sackint.intmodexp(3, -1, 11) == 4
    assert sackint.intmodexp(3, -2, 11) == 5
    assert sackint.intmodexp(3, 5, 11) == 1
    assert sackint.intmodexp(3, 9, 11) == 4
    assert sackint.intmodexp(3, 10, 11) == 1

def test_intmodrecip():
    assert sackint.intmodrecip(1, 11) == 1
    assert sackint.intmodrecip(2, 11) == 6
    assert sackint.intmodrecip(7, 11) == 8
    with pytest.raises(ValueError):
        sackint.intmodrecip(2, 4)

def test_factorial():
    assert sackint.factorial(0) == 1
    assert sackint.factorial(1) == 1
    assert sackint.factorial(2) == 2
    assert sackint.factorial(3) == 6
    assert sackint.factorial(4) == 24
    assert sackint.factorial(5) == 120
    assert sackint.factorial(37) == 13763753091226345046315979581580902400000000
    with pytest.raises(ValueError):
        sackint.factorial(-1)
    with pytest.raises(TypeError):
        sackint.factorial(8.5)

def test_num_ptns():
    assert sackint.num_ptns(-2) == 0
    assert sackint.num_ptns(-1) == 0
    assert sackint.num_ptns(0) == 1
    with pytest.raises(TypeError):
        sackint.num_ptns(1.5)

    assert sackint.num_ptns(1) == 1
    assert sackint.num_ptns(2) == 2
    assert sackint.num_ptns(3) == 3
    assert sackint.num_ptns(4) == 5
    assert sackint.num_ptns(5) == 7
    assert sackint.num_ptns(30) == 5604

def test_num_ptnsm():
    assert sackint.num_ptnsm(30, 30) == 5604
    assert sackint.num_ptnsm(30, 29) == 5603
    assert sackint.num_ptnsm(30, 28) == 5602
    assert sackint.num_ptnsm(30, 15) == 5096
    assert sackint.num_ptnsm(30, 5) == 674
    assert sackint.num_ptnsm(30, 2) == 16
    assert sackint.num_ptnsm(30, 1) == 1
    assert sackint.num_ptnsm(30, 0) == 0

def test_ptns():
    assert sackint.ptns(0) == [[]]
    assert sackint.ptns(1) == [[1]]
    assert sackint.ptns(2) == [[1, 1], [2]]
    assert sackint.ptns(3) == [[1, 1, 1], [2, 1], [3]]
    assert sackint.ptns(4) == [[1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1], [4]]

def test_ptnsm():
    assert sackint.ptnsm(4,0) == []
    assert sackint.ptnsm(4,1) == [[1, 1, 1, 1]]
    assert sackint.ptnsm(4,2) == [[1, 1, 1, 1], [2, 1, 1], [2, 2]]
    assert sackint.ptnsm(4,3) == [[1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1]]
    assert sackint.ptnsm(4,4) == [[1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1], [4]]
    assert sackint.ptnsm(4,5) == [[1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1], [4]]
