# blazefunc.py
# 
# 
# Description:
# ------------
""" File to describe the Blaze function and make it implementable
	into crifors. Input should be in wavelengths [nm], order m, alpha angle of 
	echelle [deg], gamma angle of echelle [deg] and blaze angle theta of the 
	echelle [deg]. Output will be the blaze efficiency and the blaze-
	wavelength where the effeciency has its peak.
	"""

# -------------------------------------------------------------------- #
import numpy as np


def blaze_func(wavelength, m, Echelle_angle, sigma_echelle, gamma_echelle, blaze_angle):
	
	""" Converting variabels to proper units """
	sigma_echelle = 1e6/sigma_echelle			# nm
	alpha = Echelle_angle * np.pi/180			# rad
	gamma_echelle = gamma_echelle * np.pi/180	# rad
	theta_blaze = blaze_angle * np.pi/180		# rad
	
	beta = np.arcsin( (m * wavelength) / (sigma_echelle * np.cos(gamma_echelle)) - np.sin(alpha))
	lambda_blaze = 2 * sigma_echelle * np.cos(gamma_echelle) * np.sin(theta_blaze) / m
	nu = (np.pi * sigma_echelle * np.cos(theta_blaze) / wavelength) * (np.sin(beta - theta_blaze) + np.sin(alpha - theta_blaze))
	blaze_eff = (np.sin(nu) * np.sin(nu)) / (nu * nu)

	return blaze_eff, lambda_blaze








