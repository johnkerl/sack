#!/usr/bin/python -Wall

# ================================================================
# Please see LICENSE.txt in the same directory as this file.
# John Kerl
# kerl.john.r@gmail.com
# 2007-05-31
# ================================================================

# Group module for the dihedral group parameterized by m and n.

import metacyc_tm

def get_elements_str(params_string):
    [p, q, t] = metacyc_tm.params_from_string(params_string)
    pq = p * q
    elts = []
    for i in range(0, p):
        for j in range(0, q):
            elts.append(metacyc_tm.metacyc_t(i, j, p, q, t))
    return elts
