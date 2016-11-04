#!/usr/bin/env python2

import sys, os
import logging
import subprocess
import crifors

SCRIPTDIR = os.path.dirname(os.path.realpath(__file__))
OUTDIR = os.path.join(SCRIPTDIR, 'refdata')
FNAME_BASE = os.path.join(OUTDIR,'CR2RES_REF_')
NRAYS = '1E5'
OPTS = ['--spread', '--nrays=%s'%NRAYS, '--blaze']

setups = [\
['P','gaussian'],
['P','polarimeter'],
['P','uniform'],
['F','uniform'],
['F','decker1'],
['F','decker2'],
['E','decker1'],
['E','decker2'],
#['T','decker1'],
#['T','decker2'],
]

if len(sys.argv) < 2:
    std_settings = crifors.paths.std_settings.keys()
else:
    std_settings = sys.argv[1:]

for sett in std_settings:
    # skip L & M for now
    if sett.startswith('L') or sett.startswith('M'):
        continue

    for setup in setups:
        spec, psf = setup
        sname = sett.replace('/','')
        fname = FNAME_BASE + '%s_%s_%s'%(sname,spec,psf) # '.fits.gz' gets added by crifors
        print fname
        for ext in ['.log', '.fits.gz']:
            if os.path.exists(fname+ext):
                os.unlink(fname+ext)

        argv = [sett, spec, "--psf=%s"%psf, "--outfn='%s'"%fname] + OPTS
        subprocess.call(['./crifors.py'] + argv)


#    logger.removeHandler(hdlr)
