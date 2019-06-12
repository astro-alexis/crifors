#!/usr/bin/env python3

import sys
from astropy.io import fits
import numpy as np

X = np.arange(2048)

# open a second time with fomula intact
for tracefile in sys.argv[1:]:
    print("\nfile: ", tracefile)
    trace = fits.open(tracefile)

    for i in [1,2,3]:
        tdata = trace['CHIP%s.INT1'%i].data
        maxtracenb = max([foo[4] for foo in tdata])
        for alla, order, tracenb in zip(tdata['All'],tdata['Order'],tdata['TraceNb']):
            y = np.polyval(alla[::-1],X)[1024]
            print('order, traceNb, ycen:', order, tracenb, y)


