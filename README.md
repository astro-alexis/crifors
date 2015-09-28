# __CRIFORS__
# (CRIRES+ Forward Simulator)
### version 0.2.0
----

![VLT - Paranal Observatory, Chile](http://upload.wikimedia.org/wikipedia/commons/e/ee/The_VLT%C2%B4s_Laser_Guide_Star.jpg)

------------------------------
# Prerequisites/Requirements

- GCC
- GNU Make
- [GNU Scientific Library 1.16+](http://ftp.u-tx.net/gnu/gsl/ "GSL")
- SAO-DS9 (optional, for viewing output __FITS__)
- Python 2.7 (see below)
    + NumPy 1.7+
    + Scipy 0.12+
    + Matplotlib 1.1+
    + Astropy 0.3+

In order to facilitate the compatibility of required Python packages,
an installation of the [Anaconda Python Distribution](https://store.continuum.io/cshop/anaconda/ "Anaconda Python Distribution")
is highly recommended as it contains all required packages.
The academic license is free, and installation does not require root priveledges.

------------------------------
# Setup

## make
Before running, the C source code must be compiled.
This can be done simply by typing in the terminal:

	make

## cleaning the crifors directory

	make clean

This command will remove all backup and compiled files so that the directory
reverts back to its original state.

------------------------------
# Examples

## get help / list options

A detailed list of argument options and their explanations can be found
by typing

	python crifors.py -h
or

	python crifors.py --help

# spectral band

	python crifors.py Y

This simple command will produce a simulated Y band image of an included
PHOENIX synthetic spectra (Husser et al. 2013).
The output will be directed to the `output` directory.
Note that this is the default setting, and is equivalent to the commands

	python crifors.py Y p

and

	python crifors.py Y phoenix

# input spectra

Input spectra can either be specified in a single file (fits or txt),

	python crifors.py Y </path/to/spectrum.fits>

or by 2 separate files:

    python crifors.py Y </path/to/wavelength.fits> </path/to/flux.fits>

The wavelengths units must be in [nm].  If they are not (ie. Angstroms),
a `--factor` can be passed to convert it to nm.

    python crifors.py Y </path/to/wavelength.fits> </path/to/flux.fits> --factor=0.1


In addition to supplied input spectra and the included PHOENIX model, the
following sources can be input as well:

## flatfield
With the flatfield source, `f`, `F` or `flatfield`, an ideal flatfield spectrum
is fed into the spectrograph.  It assumes a continuous, uniform distribution.

	python crifors.py Y F

## wavemap
Not implemented yet.

With the wavemap source, `w`, `W` or `wavemap`, pixel values will be wavelengths
instead of counts.



# command line options

A few often-used opions are offered as command line options as described in the
following. For full control you need to supply a config file.

## input config file

A config file of instrument and simulation can be passed to override default
settings. The distributed `config.cfg` is an exact copy of the default cfg file,
but settings can be
changed, such as detector offsets and rotation, or noise levels.
Additionally, any file of the same style may be given to `--config`.
Not all settings must be listed in the config file ie. it is okay to list
only detector settings.

	python crifors.py Y </path/to/spectrum.fits> --config=<path/to/config.cfg>

## psf
In this context we mean by PSF the distribution of light in the slit, when it
gets populated with rays. The choice is made via `--psf` with one of the
following values:

+ `gaussian` (default) - a 2d-Gaussian with its width according to `--seeing`
 (see below).
+ `uniform` - uniform flat distribution, filling the whole slit. Useful for
flatfields.
+ `decker1` - as `uniform`, but blocking the second and fourth quadrant of the
slit, counted from the top.
+ `decker2` - as `decker1`, but blocking the first and third slit quarter.

## seeing

Seeing is represented by the FWHM of a gaussian, with a default of 1.5
arcseconds.
It can be changed with the `--seeing` option:

	python crifors.py Y </path/to/spectrum.fits> --seeing=2.0


## echelle angle

The echelle angle can be changed by the `--echang` option. ~~Note that with
`--model=interp`, it can only be given in increments of 0.5 from 60.0 to 70.0~~
with a default of 63.5:

	python crifors.py Y </path/to/spectrum.fits> --echang=64.1

## noise

Shot noise is inherent in the implementation of the simulation.
However, in order to produce readout noise and dark current, the `--noise`
flag must be passed:

	python crifors.py Y </path/to/spectrum.fits> --noise

## number of input rays

The input number of rays (default 1e7) can be specified by the `--nrays`
option:

	python crifors.py Y </path/to/spectrum.fits> --nrays=1e8

Note that this increases memory consumption.  If a large number is needed,
this can be alleviated by using the `--nruns` option, where each simulation
run would be equal to `nrays`.

	python crifors.py Y </path/to/spectrum.fits> --nrays=1e8 --nruns=20

would be the same as

	python crifors.py Y </path/to/spectrum.fits> --nrays=2e9

## radial velocity shift

The input spectra can be shifted by a given radial velocity in [m/s] using the
`--rv` option:

	python crifors.py Y </path/to/spectrum.fits> --rv=3.0

## slit width

The width of the slit can either be 0.2 (default) or 0.4 arcseconds.
This is controlled by the `--slit-width` option:

	python crifors.py Y </path/to/spectrum.fits> --slit-width=0.4

## spread
This option convolves each ray with a kernel.  The advantage of this is that it
can produce a higher SN image with less computational time.

    python crifors.py Y --spread

## telluric lines

The following telluric line species calculated by LBLRTM (see Husser & Ulbrich, 2014) are included:

+ CH4
+ CO2
+ H2O
+ N2O
+ O2
+ O3

The flag can be entered as follows:

	python crifors.py Y </path/to/spectrum.fits> --telluric

------------------------------
# TODO
 * physical model w/ blaze function
   it seems that the problem here lies with inconsistent instrument parameters
 * polarimeter mode
 * background light file
 * ~~slit decker mask~~
 * ~~config file input~~
 * ~~input echelle angle interpolation~~

------------------------------
# WISH LIST
 * time variation of parameters (slit psf center, seeing, etc.)?
 * slit sky background?
 * multiprocessing? (this will require significant reworking if using `multiprocessing` module; otherwise could use `pathos`, but still much work)
 * individual parameters by command line
