#!/usr/bin/env python2

import sys, os
from pylab import *

wav = linspace(1400E-9, 2000E-9, 2E5)
hc2=1.191043E-16 #kg m^4/s^3
hc=1.98E-25 # Jm
K=1.38E-23 # J/K

def planck(wav,temp):
    return hc2 / wav**5 / (exp(hc/(wav*temp*K)) -1)

pl = planck(wav,800)+ planck(wav,3000)/800
pl /= pl.max()

args = sys.argv[1:]
fname = args[0] if args else 'data/spectra/flatfield/twoplanck.dat'
savetxt(fname, zip(wav*1E9,pl), delimiter=' ', newline='\n', fmt='%.5e')


#plot(planck(wav,100))
#show()
