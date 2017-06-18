#!/usr/bin/env python2

import sys, os, glob
import multiprocessing
import subprocess

def work(cmd):
    return subprocess.call(cmd, shell=True)

pool = multiprocessing.Pool(8)

flats = glob.glob('CRIFORS_*_F_uniform.fits')
pool.map(work, ['esorex cr2res_util_trace '+flat for flat in flats])

