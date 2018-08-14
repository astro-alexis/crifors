#!/usr/bin/env python2

import sys, os
import logging
import crifors
import multiprocessing
import subprocess

SCRIPTDIR = os.path.dirname(os.path.realpath(__file__))
OUTDIR = '/scratch/refdata'
FNAME_BASE = os.path.join(OUTDIR,'CRIFORS_')
NRAYS = '5E8'
OPTS = ['--spread', '--nrays=%s'%NRAYS, '--blaze', '--noise']

setups = [\
['P','gaussian'],
['P','polarimeter'],
#['P','uniform'],
['F','uniform'],
['F','decker1'],
#['F','decker2'],
['E','uniform'],
['E','decker1'],
#['E','decker2'],
['T','uniform'],
['T','decker1'],
#['T','decker2'],
#['G','uniform'],
#['G','decker1'],
#['G','decker2'],
]

if len(sys.argv) < 2:
    std_settings = crifors.paths.std_settings.keys()
else:
    std_settings = sys.argv[1:]

cmd_list = []

for sett in std_settings:
    if sett.startswith('L') or sett.startswith('M'):
        continue     # skip L & M for now

    for setup in setups:
        spec, psf = setup

        if sett.startswith('Y') and spec.upper() == 'T':
            continue # The ThAr starts in J band only.

        if spec.upper()=='G' and not (sett.startswith('H') \
                            or sett.startswith('K')):
            continue # gas cell is HK only

        sname = sett.replace('/','')
        fname = FNAME_BASE + '%s_%s_%s'%(sname,spec,psf) # '.fits' gets added by crifors
        if os.path.exists(fname+'.fits'):
            #os.unlink(fname+ext)
            print 'skip, %s exists'%fname
            continue

        argv = ["--psf=%s"%psf, '--outfn="%s"'%fname] + OPTS + [sett, spec]
        cmd_list.append(argv)


log = crifors.prepare_logging()
def work(cmd):
    crifors.main(log,cmd)
    #return subprocess.call(cmd, shell=True)


print cmd_list


pool = multiprocessing.Pool(5)

pool.map(work, cmd_list)


#    logger.removeHandler(hdlr)
