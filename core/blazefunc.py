# blazefunc.py
# 
# 
# Description:
# ------------
""" File to describe the Blaze function and make it implementable
	into crifors. Input should be in wavelengths [nm], order m, alpha 
	angle of echelle [deg], sigma echelle [mm^-1], gamma angle of
	echelle [deg] and blaze angle theta of the echelle [deg]. Output
	will be the blaze efficiency and the blaze wavelength where the 
	effeciency has its peak.
	
	Updated version also includes an alternative version of the blaze-
	function, which is based on the blaze equations of Marvin's
	thesis instead of Tino's excel-arc. The difference is small, but the
	alternative version is more closely centered on the blaze wavelength.	
	"""

# -------------------------------------------------------------------- #
import numpy as np


def blaze_func(wavelength, m, Echelle_angle, sigma_echelle_inv, gamma_echelle, blaze_angle):
	
	""" Converting variabels to proper units """
	sigma_ech = 1e6/sigma_echelle_inv		# nm
	alpha = Echelle_angle * np.pi/180		# rad
	gamma_ech = gamma_echelle * np.pi/180	# rad
	theta_blaze = blaze_angle * np.pi/180	# rad
	theta = alpha - theta_blaze				# rad
	D_alpha_ech = -3.23 * np.pi/180			# rad
	
	""" Approximated values obtained from Tino's excel-arc. """
	#pi = 3.1415927
	#sigma_ech = 31600						# nm
	#alpha = Echelle_angle * pi/180			# rad
	#gamma_ech = gamma_echelle * pi/180		# rad
	#theta_blaze = blaze_angle * pi/180		# rad
	#theta = alpha - theta_blaze			# rad
	#D_alpha_ech = -3.23 * pi/180			# rad	

	""" Blaze function that mimics the equations from Tino's excel-arc. """
#	beta = np.arcsin(wavelength * m / sigma_ech - np.sin(alpha)) - D_alpha_ech - alpha
#	nu = np.pi * sigma_ech * np.cos(alpha) * (np.sin(theta) + np.sin(alpha + D_alpha_ech + beta - theta_blaze)) / (wavelength * np.cos(theta))

	""" Alternative version of the blaze-function. 
	More closely aligned on the blaze wavelength than Tino's version. """
	beta = np.arcsin( (m * wavelength) / (sigma_ech * np.cos(gamma_ech)) - np.sin(alpha))	
	nu = (np.pi * sigma_ech / wavelength) * (np.sin(beta-theta_blaze) + np.sin(alpha-theta_blaze))

	blaze_eff = (np.sin(nu) * np.sin(nu)) / (nu * nu)
	lambda_blaze = 2 * sigma_ech * np.cos(gamma_ech) * np.cos(theta) * np.sin(theta_blaze) / m

	return blaze_eff, lambda_blaze
