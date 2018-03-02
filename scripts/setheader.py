#!/usr/bin/env python3
from sys import argv
import astropy.io.fits as fits

argv.pop(0)
if argv[0].startswith('-'):
    ext = int(argv[0][-1])
    argv.pop(0)
else:
    ext=0

key=argv.pop(0)
val=argv.pop(0)

for fname in argv:
    print(fname)
    f = fits.open(fname)
    f[ext].header[key]=val
    f.writeto(fname,overwrite=True)
