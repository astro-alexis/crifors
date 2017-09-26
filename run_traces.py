#!/usr/bin/env python3

import sys, os, glob
import multiprocessing
import subprocess

def work(cmd):
    print(cmd)
    return subprocess.call(cmd, shell=True)

pool = multiprocessing.Pool(12)

files = glob.glob('CRIFORS_*_F_uniform.fits')
files += glob.glob('CRIFORS_*_F_decker1.fits')
files += glob.glob('CRIFORS_*_F_decker2.fits')

for file in files.copy():
    if os.path.exists(file.replace('.fits','_trace.fits')):
        files.remove(file)
pool.map(work, ['esorex cr2res_util_trace '+file for file in files])


files = glob.glob('CRIFORS_*_trace.fits')
for file in files.copy():
    if os.path.exists(file.replace('_trace.fits','_trace_extr1D.fits')):
        files.remove(file)

pool.map(work, ['esorex cr2res_util_extract --height=20 %s %s'%(file.replace('_F_','_E_').replace('_trace',''), 
                        file) for file in files])
pool.map(work, ['esorex cr2res_util_extract --height=20 %s %s'%(file.replace('_F_','_G_').replace('_trace',''), 
                        file) for file in files])
pool.map(work, ['esorex cr2res_util_extract --height=20 %s %s'%(file.replace('_F_','_T_').replace('_trace',''), 
                        file) for file in files])


files = glob.glob('CRIFORS_*_extr1D.fits')
for file in files.copy():
    if os.path.exists(file.replace('_extr1D.fits','_extr1D_wave.fits')):
        files.remove(file)

gas = [file for file in files if '_G_' in file]
etas = [file for file in files if '_E_' in file]
lines = [file for file in files if '_T_' in file]
pool.map(work, ['esorex cr2res_util_wave --data_type="LAMP" %s %s %s'\
        %(file, file.replace('_T_','_F_').replace('_extr1D','_trace'), 'cr2res_util_genlines.fits')
                        for file in lines])
pool.map(work, ['esorex cr2res_util_wave --data_type="ETALON" %s %s'\
        %(file, file.replace('_E_','_F_').replace('_extr1D','_trace') )
                        for file in etas])


files = glob.glob('CRIFORS_*_wave.fits')
for file in files.copy():
    if os.path.exists(file.replace('_wave.fits','_wave_tilt.fits')):
        files.remove(file)

pool.map(work, ['esorex cr2res_util_tilt %s'%file for file in files])
