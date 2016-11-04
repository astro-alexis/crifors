#!/usr/bin/env python2

import sys, os
import logging
import subprocess
import crifors

SCRIPTDIR = os.path.dirname(os.path.realpath(__file__))
OUTDIR = os.path.join(SCRIPTDIR, 'refdata')
FNAME_BASE = os.path.join(OUTDIR,'CR2RES_REF_')
NRAYS = '1E6'
OPTS = ['--spread', '--nrays=%s'%NRAYS, '--blaze']

# LOOPS
# bands = ['Y', 'J', 'H', 'K', 'L', 'M']
psfs = ['gaussian', 'polarimeter', 'uniform', 'decker1', 'decker2']
inspectra = ['P', 'F', 'E']#, 'T']

if len(sys.argv) < 2:
    std_settings = crifors.paths.std_settings.keys()
else:
    std_settings = sys.argv[1:]

# LOGGING
#logger = logging.getLogger()
#formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#logger.setLevel(logging.DEBUG)

for sett in std_settings:
 for spec in inspectra:
  for psf in psfs:
    sname = sett.replace('/','')
    fname = FNAME_BASE + '%s_%s_%s'%(sname,spec,psf) # '.fits.gz' gets added by crifors
    print fname
    for ext in ['.log', '.fits.gz']:
        if os.path.exists(fname+ext):
            os.unlink(fname+ext)
#    hdlr = logging.FileHandler(fname+'.log')
#    hdlr.setFormatter(formatter)
#    logger.addHandler(hdlr)

    argv = [sett, spec, "--psf=%s"%psf, "--outfn='%s'"%fname] + OPTS
    subprocess.call(['./crifors.py'] + argv)


#    logger.removeHandler(hdlr)