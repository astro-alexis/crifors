#!/usr/bin/env python2

import sys, os, glob
import multiprocessing
import subprocess

def work(cmd):
    return subprocess.call(cmd, shell=True)

pool = multiprocessing.Pool(12)

flats = glob.glob('CRIFORS_*_F_uniform.fits')
for flat in flats:
    if os.path.exists(flat.replace('.fits','_trace.fits')):
        flats.remove(flat)

pool.map(work, ['esorex cr2res_util_trace '+flat for flat in flats])

