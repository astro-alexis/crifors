#!/usr/bin/env python3

import sys
from astropy.io import fits as F
from openpyxl import load_workbook

wb = load_workbook(sys.argv[1], data_only=True)
cfg = wb['cpmcfgWVLEN_Table.csv']
fitskeys= [c.value for c in cfg.rows[5]] # 6th row has FITS header names
setting_col = 2       # 3rd column is std setting name
colnames = [c.value for c in cfg.rows[0]]
isdet1 = [str(n).lower().endswith('det1') for n in colnames]
isdet2 = [str(n).lower().endswith('det2') for n in colnames]
isdet3 = [str(n).lower().endswith('det3') for n in colnames]

fitsname = sys.argv[2]
with F.open(fitsname) as hdulist:
    std = hdulist[0].header['HIERARCH ESO INS WLEN ID']
    try:
        assert(len(std.split('/'))==3)
    except:
        print("The input file has no standard-setting info!")
        sys.exit()

    # clear WLEN headers
    for i in range(10):
        for hdu in hdulist:
            for key in hdu.header.keys():
                if 'WLEN' in key:
                    del hdu.header[key]

    for row in cfg.rows:
        if row[setting_col].value != std:
            continue

        values = [c.value for c in row]
        for key,val,d1,d2,d3 in zip(fitskeys,values,isdet1,isdet2,isdet3):
            if key and not '?' in key:
                if val==None or val=='':
                    continue #skip key of no value!

                for i,hdu in enumerate(hdulist):
                    chip = hdu.header.get('EXTNAME','0')[-1]
                    k = 'HIERARCH ESO '+key.replace('.',' ')
                    if d1 and chip=='1':
                        hdu.header[k] = val
                    elif d2 and chip=='2':
                        hdu.header[k] = val
                    elif d3 and chip=='3':
                        hdu.header[k] = val

                    elif (chip=='0') and not (d1 or d2 or d3):
                        hdu.header[k] = val


    hdulist.writeto(fitsname, overwrite=True)
