#!/usr/bin/env python2

import sys, os
import logging

import crifors

SCRIPTDIR = os.path.dirname(os.path.realpath(__file__))
OUTDIR = os.path.join(SCRIPTDIR, 'refdata')
FNAME_BASE = os.path.join(OUTDIR,'CR2RES_REF_')
baseopts = ['--spread', '--nrays=1E7', '--blaze']

# LOOPS
bands = ['H', 'K', ]

# LOGGING
logger = logging.getLogger('gen_ref_data')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logger.setLevel(logging.DEBUG)


for band in bands:
    print band
    logname = FNAME_BASE + band + '.log'
    fitsname = FNAME_BASE + band # '.fits.gz' gets added by crifors
    for f in [logname, fitsname+'.fits.gz']:
        if os.path.exists(f):
            os.unlink(f)
    hdlr = logging.FileHandler(logname)
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)

    argv = [band] + baseopts + ["--outfn='%s'"%fitsname]
    logger.info('argv: ' + str(argv))
    crifors.main(log=logger, argv=argv)


    logger.removeHandler(hdlr)
