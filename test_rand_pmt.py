#!/usr/bin/python -Wall

# ================================================================
# Please see LICENSE.txt in the same directory as this file.
# John Kerl
# kerl.john.r@gmail.com
# 2007-05-31
# ================================================================

import sys,copy
import pmtc_tm
import pmti_tm

#count=80000
count=100000
#N=100
N=6
do_bad = False
if len(sys.argv) >= 2:
    N = int(sys.argv[1])
if len(sys.argv) == 3:
    do_bad = True

for i in range(0, count):
    if do_bad:
        pi = pmtc_tm.bad_rand_pmtc(N)
    else:
        pi = pmtc_tm.rand_pmtc(N)
    #ct = pi.cycle_type()
    #print ct
    print(pi)
