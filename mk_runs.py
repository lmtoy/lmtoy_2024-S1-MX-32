#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-32"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["G38.60"] =  [ 112902,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["G38.60"] = "dv=20 dw=20"


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["G38.60"] = "pix_list=-13"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3["G38.60"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
