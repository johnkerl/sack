#!/usr/bin/python -Wall

# ================================================================
# Please see LICENSE.txt in the same directory as this file.
# John Kerl
# kerl.john.r@gmail.com
# 2007-05-31
# ================================================================

# Group module for the T group.

import T_tm

def get_elements_str(params_string: str):
    elts = []
    for i in range(0, 3):
        for j in range(0, 4):
            elt = T_tm.T_t(i, j)
            elts.append(elt)
    return elts
