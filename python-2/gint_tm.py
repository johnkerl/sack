#!/usr/bin/python -Wall

# ================================================================
# Please see LICENSE.txt in the same directory as this file.
# John Kerl
# kerl.john.r@gmail.com
# 2007-05-31
# ================================================================

# Type module for Gaussian integers (m+ni for integer m,n).

import re
import copy

import sackint

class gint_t:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __eq__(a,b):
        if (a.re != b.re):
            return 0
        if (a.im != b.im):
            return 0
        return 1

    def __ne__(a,b):
        return not (a == b)

    def __add__(a,b):
        c = gint_t(a.re + b.re, a.im + b.im)
        return c

    def __sub__(a,b):
        c = gint_t(a.re - b.re, a.im - b.im)
        return c

    def __mul__(a,b):
        # (ar, ai) * (br, bi)
        c = gint_t(a.re*b.re - a.im*b.im, a.re*b.im + a.im*b.re)
        return c

    # Grove's _Algebra_, p. 65
    # (ar, ai)   (ar, ai)(br, -bi)    a * conj(b)
    # -------- = ----------------- = -----------
    # (br, bi)   (br, bi)(br, -bi)    norm b
    #
    # Then, take the *nearest* integers to the rational coordinates.

    def __div__(a,b):
        numer = a * b.conj()
        denom = b.norm()
        Qre = (1.0 * numer.re) / denom
        Qim = (1.0 * numer.im) / denom
        Zre = int(round(Qre))
        Zim = int(round(Qim))
        q = gint_t(Zre, Zim)
        return q

    def __mod__(a,b):
        q = a / b
        return a - (q * b)

    def conj(a):
        return gint_t(a.re, -a.im)

    def norm(a):
        return a.re*a.re + a.im*a.im

    def scan(self, string):
        strings = re.split(',', string)
        n = len(strings)
        if (n == 1):
            self.re = int(strings[0])
        elif (n == 2):
            self.re = int(strings[0])
            self.im = int(strings[1])
        else:
            raise IOError

    def __str__(self):
        string = str(self.re) + "," + str(self.im)
        return string

    def __repr__(self):
        return self.__str__()

#def from_string(value_string, params_string):
#   if (len(params_string) == 0):
#       print "Modmul requires non-empty parameter string"
#   obj = gint_t([1], [1])
#   obj.scan(value_string, params_string)
#   return obj

#a = gint_t(7,-3)
#b = gint_t(5,3)
#sum = a+b
#diff = a-b
#prod = a*b
#q = a/b
#r = a%b
#print a, "+", b, "=", sum
#print a, "-", b, "=", diff
#print a, "*", b, "=", prod
#print a, "/", b, "=", q
#print a, "%", b, "=", r
#print "qb+r", q*b + r

print()


a = gint_t(7,-3)
b = gint_t(5,3)

for i in range(0,10):
    if (b.norm() == 0):
        break
    q = a/b
    r = a%b
    print((a, b, q, r))
    a = b
    b = r


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

        def test___add__(self):
            pass # to be implemented

        def test___sub__(self):
            pass # to be implemented

        def test___mul__(self):
            pass # to be implemented

        def test___div__(self):
            pass # to be implemented

        def test___mod__(self):
            pass # to be implemented

        def test_conj(self):
            pass # to be implemented

        def test_norm(self):
            pass # to be implemented

        def test_scan(self):
            pass # to be implemented

        def test___str__(self):
            pass # to be implemented

        def test___repr__(self):
            pass # to be implemented

    # ----------------------------------------------------------------
    unittest.main()
