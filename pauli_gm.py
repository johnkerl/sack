#!/usr/bin/python -Wall

# ================================================================
# Please see LICENSE.txt in the same directory as this file.
# John Kerl
# kerl.john.r@gmail.com
# 2007-05-31
# ================================================================

# Group module for the Pauli matrices.

import pauli_tm
import sackgrp

def get_elements_str(params_string):
    elts = []
    elts.append(pauli_tm.from_string("sx",""))
    elts.append(pauli_tm.from_string("sy",""))
    elts.append(pauli_tm.from_string("sz",""))
    sackgrp.close_group(elts)
    return elts
