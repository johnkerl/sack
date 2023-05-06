#!/usr/bin/python -Wall

# ================================================================
# Please see LICENSE.txt in the same directory as this file.
# John Kerl
# kerl.john.r@gmail.com
# 2007-05-31
# ================================================================

# Group module for alternating permutations A_n, using cycle-decomposition I/O.

import pmtc_tm
import sackint

def get_elements(n):
    sn_size = sackint.factorial(n)
    elts = []
    for k in range(0, sn_size):
        elt = pmtc_tm.kth_pmtc(k, n, sn_size)
        if (elt.parity() == 0):
            elts.append(elt)
    pmtc_tm.sort_pmtcs(elts)
    return elts

def get_elements_str(params_string):
    n = pmtc_tm.params_from_string(params_string)
    return get_elements(n)
