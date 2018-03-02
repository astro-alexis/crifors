#!/usr/bin/env python3

import sys, os
import astropy.io.fits as fits

fname = sys.argv[1]
f = fits.open(fname)
inhead = f[0].header
rawexp = int(inhead['EXPTIME'])
ndit = int(inhead['ESO DET NDIT'])
data = f[0].data
nxy=2048

header = inhead.copy()
header['HIERARCH ESO DPR TECH'] = ('IMAGE')
header['HIERARCH ESO DPR CATG'] = ('CALIB', 'Observation category')
header['HIERARCH ESO DPR TYPE'] = ('DARK', 'Observation type')

for i in range(ndit):
    #header['EXPTIME'] = ('%d'%(rawexp*i), 'Total exposure time')
    prim = fits.PrimaryHDU(header=header)
    one = fits.ImageHDU(data=data[i, :, 0:nxy])
    two = fits.ImageHDU(data=data[i, :, nxy:2*nxy])
    tre = fits.ImageHDU(data=data[i, :, 2*nxy:])
    fits.HDUList([prim, one, two, tre]).writeto('CRIRES_DARK_500_%02d.fits'%i,
        overwrite=True)
