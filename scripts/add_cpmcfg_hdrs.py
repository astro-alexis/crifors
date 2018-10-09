#!/usr/bin/env python3

import sys
from astropy.io import fits as F
from openpyxl import load_workbook

wb = load_workbook(sys.argv[1], data_only=True)
cfg = wb['crmcfgWLEN.txt']
rows=list(cfg.rows)
fitskeys= [c.value for c in rows[5]] # 6th row has FITS header names
setting_col = 2       # 3rd column is std setting name
colnames = [c.value for c in rows[0]]

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
        for key,val in zip(fitskeys,values):
            if not key: continue
            tmp = key.split(':')
            if len(tmp)==1: # no prefix means primary header
                det = None
            elif len(tmp)==2: # extension is given before colon
                det,key = tmp
            else:
                raise ValueError('Unknown key format')
            if key and not '?' in key:
                if val==None or val=='':
                    continue #skip key if no value!

                for i,hdu in enumerate(hdulist):
                    chip = hdu.header.get('EXTNAME','0')[-1]
                    k = 'HIERARCH ESO '+key.replace('.',' ')
                    if det == chip:
                        hdu.header[k] = val
                    elif det is None:
                        hdu.header[k] = val


    hdulist.writeto(fitsname, overwrite=True)
