#!/usr/bin/python -Wall

# ================================================================
# Please see LICENSE.txt in the same directory as this file.
# John Kerl
# kerl.john.r@gmail.com
# 2007-05-31
# ================================================================

# Type module for the dihedral group on n vertices.

import re

class dih_t:

    def __init__(self, argrot, argflip, argn):
        self.n    = argn
        self.rot  = argrot  % self.n
        self.flip = argflip & 1

    def __eq__(a,b):
        return ((a.rot == b.rot) and (a.flip == b.flip))

    def __ne__(a,b):
        return not (a == b)

    def __mul__(a,b):
        if (a.n != b.n):
            raise RuntimeError
        if (a.flip):
            crot = a.rot - b.rot
        else:
            crot = a.rot + b.rot
        c = dih_t(crot, a.flip ^ b.flip, a.n)
        return c

    def inv(a):
        if (a.flip):
            c = dih_t(a.rot, a.flip, a.n)
            return c
        else:
            c = dih_t(a.n - a.rot, a.flip, a.n)
            return c

    def scan(self, string, argn):
        groups = re.match(r"^(\d)+,(\d+)$", string).groups();
        if len(groups) != 2:
            raise IOError
        self.__init__(int(groups[0]), int(groups[1]), argn)

    def __str__(self):
        return str(self.rot) + "," + str(self.flip)

    def __repr__(self):
        return self.__str__()

def params_from_string(params_string):
    n = int(params_string)
    return n

def from_string(value_string, params_string):
    n = params_from_string(params_string)
    obj = dih_t(0, 0, n)
    obj.scan(value_string, n)
    return obj


# ================================================================
import unittest
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
