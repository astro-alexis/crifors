#!/usr/bin/env python3
from sys import argv, exit
import astropy.io.fits as fits

if len(argv) < 4:
    print("./setheader Some.Key value fname [fname ...]")
    exit(0)

argv.pop(0)
if argv[0].startswith('-'):
    ext = int(argv[0][-1])
    argv.pop(0)
else:
    ext=0

key=argv.pop(0).replace('.',' ').upper()
val=argv.pop(0)
if '.' in val:
    try:
        val = float(val)
    except:
        pass
else:
    try:
        val = int(val)
    except:
        pass
print(type(val))
for fname in argv:
    print(fname)
    f = fits.open(fname)
    f[ext].header[key]=val
    f.writeto(fname,overwrite=True)
