#!/usr/bin/python -Wall

# ================================================================
# Please see LICENSE.txt in the same directory as this file.
# John Kerl
# kerl.john.r@gmail.com
# 2007-05-31
# ================================================================

# Type module for the ring of integers mod n.

import sys
import re
import copy

class mod_t:
    def __init__(self, resarray, modarray):
        self.check_lengths(len(resarray), len(modarray), "residues", "moduli")
        self.check_moduli(modarray)
        self.residues = copy.copy(resarray)
        self.moduli   = copy.copy(modarray)
        for i in range(0, len(modarray)):
            self.residues[i] %= self.moduli[i]

    def __add__(a,b):
        a.check_lengths(len(a.moduli), len(b.moduli), "moduli", "moduli")
        a.check_moduli_pair(a.moduli, b.moduli)
        c = mod_t(a.residues, a.moduli)
        for i in range (0, len(a.moduli)):
            c.residues[i] = (a.residues[i] + b.residues[i]) % c.moduli[i]
        return c

    def __sub__(a,b):
        a.check_lengths(len(a.moduli), len(b.moduli), "moduli", "moduli")
        a.check_moduli_pair(a.moduli, b.moduli)
        c = mod_t(a.residues, a.moduli)
        for i in range (0, len(a.moduli)):
            c.residues[i] = (a.residues[i] - b.residues[i]) % c.moduli[i]
        return c

    def __add__(a,b):
        a.check_lengths(len(a.moduli), len(b.moduli), "moduli", "moduli")
        a.check_moduli_pair(a.moduli, b.moduli)
        c = mod_t(a.residues, a.moduli)
        for i in range (0, len(a.moduli)):
            c.residues[i] = (a.residues[i] + b.residues[i]) % c.moduli[i]
        return c

    def __mul__(a,b):
        a.check_lengths(len(a.moduli), len(b.moduli), "moduli", "moduli")
        a.check_moduli_pair(a.moduli, b.moduli)
        c = mod_t(a.residues, a.moduli)
        for i in range (0, len(a.moduli)):
            c.residues[i] = (a.residues[i] * b.residues[i]) % c.moduli[i]
        return c

    def __eq__(a,b):
        if (len(a.residues) != len(b.residues)):
            return 0
        n = len(a.residues)
        for i in range(0, n):
            if (a.residues[i] != b.residues[i]):
                return 0
        return 1

    def __ne__(a,b):
        return not (a == b)

    def __neg__(a):
        c = mod_t(a.residues, a.moduli)
        for i in range(0, len(a.moduli)):
            c.residues[i] = (-a.residues[i]) % a.moduli[i]
        return c

    def inv(a):
        c = mod_t(a.residues, a.moduli)
        for i in range(0, len(a.moduli)):
            c.residues[i] = sackint.intmodrecip(a.residues[i], a.moduli[i])
        return c

    def scan(self, res_string, mod_array):
        res_strings = re.split(',', res_string)
        self.check_lengths(len(res_strings), len(mod_array), res_strings,
            str(mod_strings))
        n = len(res_strings)
        resarray = list(range(0, n))
        for i in range(0, n):
            resarray[i] = int(res_strings[i])
        self.__init__(resarray, modarray)

    def __str__(self):
        string = str(self.residues[0])
        for i in range(1, len(self.residues)):
            string += "," + str(self.residues[i])
        return string

    def __repr__(self):
        return self.__str__()

    def check_length(self, length, desc):
        if (length < 1):
            print((desc, "length", str(length), "< 1"))
            raise RuntimeError

    def check_lengths(self, len1, len2, desc1, desc2):
        self.check_length(len1, desc1)
        self.check_length(len2, desc2)
        if (len1 != len2):
            print((desc1, "length", str(len1), "!=", desc2, "length", len2))
            raise RuntimeError

    def check_moduli(self, mods):
        for i in range(0, len(mods)):
            if (mods[i] < 1):
                print(("Modulus", mods[i], "< 1 in", mods))
                raise RuntimeError

    def check_moduli_pair(self, mods1, mods2):
        if (mods1 != mods2):
            print(("Mismatched moduli", mods1, ", ", mods2))
            raise RuntimeError

def params_from_string(params_string):
    if (len(params_string) == 0):
        print("Modadd requires non-empty parameter string")
        sys.exit(1)
    mod_strings = re.split(',', params_string)
    n = len(mod_strings)
    mod_array = list(range(0, n))
    for i in range(0, n):
        mod_array[i] = int(mod_strings[i])
    return mod_array

def from_string(value_string, params_string):
    mod_array = params_from_string(params_string)
    obj = mod_t([1], [1])
    obj.scan(value_string, mod_array)
    return obj














#def mod_t:
#   def __init__(self, residue, modulus):
#       self.residue = copy.copy(residue) % modulus
#       self.modulus = copy.copy(modulus)
#
#   def __eq__(a,b):
#       if (a.modulus != b.modulus):
#           return 0
#       if (a.residue != b.residue):
#           return 0
#       return 1
#
#   def __ne__(a,b):
#       return not (a == b)
#
#   def __add__(a,b):
#       # xxx check moduli
#       c = mod_t(a.residue + b.residue, a.modulus)
#       return c
#
#   def __neg__(a):
#       c = mod_t(-a.residue, a.modulus)
#       return c
#
#   def __sub__(a,b):
#       # xxx check moduli
#       c = mod_t(a.residue - b.residue, a.modulus)
#       return c
#
#   def __mul__(a,b):
#       # xxx check moduli
#       c = mod_t(a.residue * b.residue, a.modulus)
#       return c
#
#   # This is an abstract inversion method, using Blankinship's extended GCD.
#   # Performance could be improved on for particular classes.
#
#   def inv(a):
#       print "mod inv stub"
#       return 0
#
##  def scan(self, res_string, mod_string):
##      xxx stub
#
#   def __str__(self):
#       string = str(self.residue)
#       return string
#
##  def check_moduli(self, mods):
##      for i in range(0, len(mods)):
##          if (mods[i] < 1):
##              print "Modulus", mods[i], "< 1 in", mods
##              raise RuntimeError
#
##def from_string(value_string, params_string):
##  if (len(params_string) == 0):
##      print "Modmul requires non-empty parameter string"
##  obj = mod_t([1], [1])
##  obj.scan(value_string, params_string)
##  return obj


# ================================================================
import unittest
if __name__ == '__main__':

    class test_cases(unittest.TestCase):
        def test___init__(self):
            pass # to be implemented

        def test___add__(self):
            pass # to be implemented

        def test___sub__(self):
            pass # to be implemented

        def test___add__(self):
            pass # to be implemented

        def test___mul__(self):
            pass # to be implemented

        def test___eq__(self):
            pass # to be implemented

        def test___ne__(self):
            pass # to be implemented

        def test___neg__(self):
            pass # to be implemented

        def test_inv(self):
            pass # to be implemented

        def test_scan(self):
            pass # to be implemented

        def test___str__(self):
            pass # to be implemented

        def test___repr__(self):
            pass # to be implemented

        def test_check_length(self):
            pass # to be implemented

        def test_check_lengths(self):
            pass # to be implemented

        def test_check_moduli(self):
            pass # to be implemented

        def test_check_moduli_pair(self):
            pass # to be implemented

        def test_params_from_string(self):
            pass # to be implemented

        def test_from_string(self):
            pass # to be implemented

    # ----------------------------------------------------------------
    unittest.main()
