#!/usr/bin/env python2

import sys, os
import astropy.io.fits as fits

RAWDIR = '/home/tom/pipes/otherdata/detetector-tests/'


SCRIPTDIR = os.path.dirname(os.path.realpath(__file__))
OUTDIR = os.path.join(SCRIPTDIR, 'refdata')
FNAME_BASE = os.path.join(OUTDIR,'CR2RES_REF_')

if len(sys.argv) < 2:
    fname = max(glob.glob(os.path.join(OUTDIR,'*')), key=os.path.getctime)
else:
    fname = sys.argv[1]

heads = [hdu.header for hdu in fits.open(fname)]
header = heads[0].copy()
header['HIERARCH ESO DPR TECH'] = ('IMAGE')
header['HIERARCH ESO DPR CATG'] = ('CALIB', 'Observation category')
header['HIERARCH ESO DPR TYPE'] = ('DARK', 'Observation type')
