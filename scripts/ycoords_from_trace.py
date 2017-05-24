#!/usr/bin/env python3

import sys
from astropy.io import fits as F
from openpyxl import load_workbook
import numpy as np

CRIFORS = "/home/tom/work/crires/crifors.git/"
wb = load_workbook(CRIFORS+'data/cpmcfgWVLEN Table.xlsx',  data_only=True)
cfg = wb['cpmcfgWLEN']
fitskeys= [c.value for c in cfg.rows[5]] # 6th row has FITS header names
setting_col = 2       # 3rd column is std setting name
X = np.arange(2048)

trace = F.open(sys.argv[1])
std = trace[0].header['HIERARCH ESO INS WLEN ID']
print(std)
assert(len(std.split('/'))==3)

for i,r in enumerate(cfg.rows):
    if r[setting_col].value == std:
        print('found row %s'%i)
        break

# open a second time with fomula intact
wb = load_workbook(CRIFORS+'data/cpmcfgWVLEN Table.xlsx')
cfg = wb['cpmcfgWLEN']
row = cfg.rows[i]

D = dict()
for key,col in zip(fitskeys,row):
    if key and key.startswith('INS.WLEN.CENY'):
        D[key] = col

for i in [1,2,3]:
    tdata = trace['CHIP%s'%i].data
    for alla, upper, lower, order, tracenb, wave in tdata:
        y = np.polyval(alla[::-1],X)[1024]
        if y and not np.isnan(y):
            D['INS.WLEN.CENY%s%s'%(9-tracenb,i)].value = y

        
wb.save('test.xlsx')
