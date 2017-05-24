#!/usr/bin/env python3

import sys
from astropy.io import fits as F
from openpyxl import load_workbook

wb = load_workbook(sys.argv[1], data_only=True)
cfg = wb['cpmcfgWLEN']
fitskeys= [c.value for c in cfg.rows[5]] # 6th row has FITS header names
setting_col = 2       # 3rd column is std setting name

with F.open(sys.argv[2]) as hdulist:
    std = hdulist[0].header['HIERARCH ESO INS WLEN ID']
    try:
        assert(len(std.split('/'))==3)
    except:
        print("The input file has no standard-setting info!")
        sys.exit()

    for row in cfg.rows:
        if row[setting_col].value != std:
            continue

        values = [c.value for c in row]
        for key,val in zip(fitskeys,values):
            if key and not '?' in key:
                if not val: val=''
                print(key,val)
                for head in [h.header for h in hdulist]:
                    head['HIERARCH ESO '+key.replace('.',' ')] = val

    hdulist.writeto('test.fits', overwrite=True)
                
