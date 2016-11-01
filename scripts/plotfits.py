#!/usr/bin/env python2

import matplotlib.pylab as plt
import pyfits
from scipy import ndimage
import sys, os, glob

DETSIZE = 2048
DETNAME = ['DL','DM','DR']
SIMHEAD = 'HIERARCH ESO SIMU '

fig = plt.figure(figsize=(12,4))
plt.subplots_adjust(0.01,0.01,0.99,0.99,0,0)

if len(sys.argv) < 2:
    # if no file given, use the latest in output/
    SCRIPTDIR = os.path.dirname(os.path.realpath(__file__))
    FITSDIR = os.path.join(SCRIPTDIR, os.path.pardir, 'output')
    fname = max(glob.glob(os.path.join(FITSDIR,'*')), key=os.path.getctime)
else:
    fname = sys.argv[1]

hdulist = pyfits.open(fname)
hdrs = hdulist[0].header
DETPIX = hdrs[SIMHEAD+'DPIX']

for i,h in enumerate(hdulist[1:]):
    nx,ny = h.header['NAXIS1'], h.header['NAXIS2']
    assert nx == ny == DETSIZE

    rotAng = hdrs[SIMHEAD+DETNAME[i]+' TAU'] *-1/2.
    xoff = hdrs[SIMHEAD+DETNAME[i]+' XD0'] / DETPIX
    yoff = hdrs[SIMHEAD+DETNAME[i]+' YD0'] / DETPIX
    cenX, cenY = i*DETSIZE + (DETSIZE/2) + xoff, DETSIZE/2 + yoff

    img = ndimage.rotate(h.data, rotAng, cval=plt.nan)
    nxr, nyr = img.shape

    plt.imshow(plt.log10(img), interpolation='nearest', cmap=plt.cm.hot,
        extent=(cenX - nxr/2.0,
                cenX + nxr/2.0,
                cenY - nyr/2.0,
                cenY + nyr/2.0
                ))

plt.axis('off')
MARGIN = DETSIZE*0.04
plt.axis((0-MARGIN, DETSIZE*3 + MARGIN, 0-MARGIN, DETSIZE+MARGIN))
plt.show()
