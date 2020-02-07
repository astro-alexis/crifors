import os.path

# DIRECTORIES
core_dir = "core"
data_dir = "data"
defaults_dir = "defaults"
output_dir = "output"
logs_dir = "logs"
codev_dir = os.path.join(data_dir, "codevtrace")
codevdata_dir = os.path.join(codev_dir, "original")
codevparsed_dir = os.path.join(codev_dir, "parsed")
spectra_dir = os.path.join(data_dir, "spectra")
phx_dir = os.path.join(spectra_dir, "phoenix")
tell_dir = os.path.join(spectra_dir, "telluric")
pol_dir = os.path.join(data_dir, "polarimeter")
eta_dir = os.path.join(spectra_dir, "etalon")
thar_dir = os.path.join(spectra_dir, "thar")
flat_dir = os.path.join(spectra_dir, "flatfield")
gas_dir = os.path.join(spectra_dir, "gascell")

# FILENAMES
codev_fn = "criresplus_%s_v6_echelle_angle_%s_order_%s.txt"
phx_waves_fn = "WAVE_PHOENIX-ACES-AGSS-COND-2011.fits"
phx_flux_fn = "lte03000-5.00-0.0.PHOENIX-ACES-AGSS-COND-2011-HiRes.fits"
output_fn = "crifors.%s"
polsep_fn = "CRIRES_%s_sep.txt"
polwave_fn = "FSR_%s.txt"
eta_fn = "etalon.npz"
thar_fn = "ThAr.dat"
flat_fn = "twoplanck.dat"
gas_fn = "SGC_template.npz"

# FULL PATHS
codevdata_path = os.path.join(codev_dir, "original", codev_fn)
codevparsed_path = os.path.join(codev_dir, "parsed", codev_fn)
codevparsednpy_path = os.path.splitext(codevparsed_path)[0] + ".npy"
phx_waves_path = os.path.join(phx_dir, phx_waves_fn)
phx_flux_path = os.path.join(phx_dir, phx_flux_fn)
polsep_path = os.path.join(pol_dir, polsep_fn)
polwave_path = os.path.join(pol_dir, polwave_fn)
eta_path = os.path.join(eta_dir, eta_fn)
thar_path = os.path.join(thar_dir, thar_fn)
flat_path = os.path.join(flat_dir, flat_fn)
gas_path = os.path.join(gas_dir, gas_fn)

# SETTINGS
dsettings_fn = "settings.cfg"
dsettings = os.path.join(defaults_dir, dsettings_fn)
tell_species = "CH4 CO2 H2O N2O O2 O3".split()


# INST PARAMS
dinst_fn = "inst.cfg"
dinst = os.path.join(defaults_dir, dinst_fn)

# STD SETTINGS
# Echelle angles for the standard settings are taken from ESO-289259 and rounded to the closest .5
# https://pdm.eso.org/kronodoc/HQ/ESO-289259/1
std_settings = {\
'Y/1/2': '65.5',
'Y/2/2': '65.5',
'J/1/3': '65.5',
'J/2/3': '65.5',
'J/3/3': '65.0',
'H/1/4': '66.0',
'H/2/4': '65.5',
'H/3/4': '65.0',
'H/4/4': '64.5',
'K/1/4': '67.0',
'K/2/4': '66.0',
'K/3/4': '65.0',
'K/4/4': '64.0',
'L/1/7': '69.0',
'L/2/7': '68.5',
'L/3/7': '67.0',
'L/4/7': '66.0',
'L/5/7': '64.5',
'L/6/7': '63.0',
'L/7/7': '62.5',
'M/1/9': '70.0',
'M/2/9': '70.0',
'M/3/9': '68.5',
'M/4/9': '67.0',
'M/5/9': '66.0',
'M/6/9': '64.5',
'M/7/9': '63.0',
'M/8/9': '62.0',
'M/9/9': '61.5',
 }
