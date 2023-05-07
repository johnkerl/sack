#!/usr/bin/python -Wall

# ================================================================
# Please see LICENSE.txt in the same directory as this file.
# John Kerl
# kerl.john.r@gmail.com
# 2007-05-31
# ================================================================

import re
import unittest

# Type module for the T group (the third nonabelian group of order 12, other
# than A4 and D6).  It may be thought of as Z3 semidirect Z4, where Z4 acts on
# Z3 by inversion.
#
# (ai, aj)(bi, bj) = (ai aj(bi), aj bj)
#
# where aj(bi) is the action of aj on bi.

class T_t:
    def __init__(self, argi, argj):
        self.i = argi % 3
        self.j = argj % 4

    def __eq__(a,b):
        return ((a.i == b.i) and (a.j == b.j))

    def __ne__(a,b):
        return not (a == b)

    def __mul__(a,b):
        ibi = b.i
        if a.j & 1:
            ibi = -ibi
        ci = (a.i + ibi) % 3
        cj = (a.j + b.j) % 4
        c = T_t(ci, cj)
        return c

    def inv(a):
        # (ai, aj)(bi, bj) = (ai aj(bi), aj bj) = (0, 0)
        # Given ai and aj, find bi and bj.
        bi = (-a.i) % 3
        if a.j & 1:
            bi = a.i % 3
        bj = (-a.j) % 4
        b = T_t(bi, bj)
        return b

    def scan(self, string):
        groups = re.match(r"^(\d)+,(\d+)$", string).groups();
        if len(groups) != 2:
            raise IOError
        self.__init__(int(groups[0]), int(groups[1]))

    def __str__(self):
        return str(self.i) + "," + str(self.j)

    def __repr__(self):
        return self.__str__()

def params_from_string(_params_string):
    return 0

def from_string(value_string, params_string):
    obj = T_t(0, 0)
    obj.scan(value_string)
    return obj


# ================================================================
if __name__ == '__main__':

    class test_cases(unittest.TestCase):
        def test___init__(self):
            pass # to be implemented

        def test___eq__(self):
            pass # to be implemented

        def test___ne__(self):
            pass # to be implemented

        def test___mul__(self):
            pass # to be implemented

        def test_inv(self):
            pass # to be implemented

        def test_scan(self):
            pass # to be implemented

        def test___str__(self):
            pass # to be implemented

        def test___repr__(self):
            pass # to be implemented

        def test_params_from_string(self):
            pass # to be implemented

        def test_from_string(self):
            pass # to be implemented

    # ----------------------------------------------------------------
    unittest.main()
