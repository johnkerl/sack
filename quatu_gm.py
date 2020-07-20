#!/usr/bin/python -Wall

# ================================================================
# Please see LICENSE.txt in the same directory as this file.
# John Kerl
# kerl.john.r@gmail.com
# 2007-05-31
# ================================================================

# Group module for the quaternion unit group.

import quatu_tm

def get_elements_str(params_string):
    not_used = quatu_tm.params_from_string(params_string)
    elts = list(range(0, 8))
    for i in range(0, 8):
        elts[i] = quatu_tm.quatu_t(i)
    return elts
