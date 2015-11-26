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
	sigma_ech = 1e6/31.6					# nm
	alpha_ech = Echelle_angle * np.pi/180	# rad
	gamma_ech = 3.8 * np.pi/180				# rad
	blaze_angle = 63.5 * np.pi/180			# rad
	theta_blaze = alpha_ech - blaze_angle	# rad
	D_alpha_ech = -3.23 * np.pi/180			# rad

	# Approximated values more closely resembling Tino's excel-arc
	#pi = 3.14159267
	#sigma_ech = 31600
	#alpha_ech=Echelle_angle * pi/180
	#gamma_ech = 3.8 * pi/180
	#blaze_angle = 63.5 * pi/180
	#theta_blaze=alpha_ech-blaze_angle
	#D_alpha_ech = -3.23 * pi/180

	beta=np.arcsin(wavelength * m / sigma_ech - np.sin(alpha_ech)) - D_alpha_ech - alpha_ech
	lambda_blaze = 2 * sigma_ech * np.cos(gamma_ech) * np.sin(blaze_angle) / m
	nu = np.pi * sigma_ech * np.cos(alpha_ech) * (np.sin(theta_blaze) + np.sin(alpha_ech + D_alpha_ech + beta - blaze_angle)) / (wavelength * np.cos(theta_blaze))
	blaze_eff = (np.sin(nu) * np.sin(nu)) / (nu * nu)

	return blaze_eff, lambda_blaze
