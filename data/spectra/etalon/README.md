provided by Ulf Seeman Feb 29 2016
wavelength rage 950-2500nm

savefile made with np.savez_compressed('etalon.npz',wav=wav,spec=spec)

reading:
data = np.load('etalon.npz')
wav = data['wav']
spec = data['spec']
