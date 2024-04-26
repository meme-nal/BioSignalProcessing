import mne
import matplotlib
matplotlib.use('GTK4Agg')

import matplotlib.pyplot as plt

# getting the raw data
raw_data = mne.io.read_raw_edf('./data/record.edf', preload=True)

# dropping bad channels
bad_channels = raw_data.ch_names[-5:-1]
bad_channels.append("SAO2-1")
raw_data = raw_data.drop_channels(bad_channels)

# renaming channels
new_names = ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'Fz', 'Cz', 'Pz']
raw_data.rename_channels(dict(zip(raw_data.ch_names, new_names)))

# making standard montage
std_montage = mne.channels.make_standard_montage('standard_1020')
raw_data.set_montage(std_montage)

eyes_closed = raw_data.copy().crop(tmin=146, tmax=161)
eyes_opened = raw_data.copy().crop(tmin=168, tmax=180)

""" Legacy code extracting alpha-rhythm
eyes_closed_alpha = eyes_closed.copy().filter(l_freq=8, h_freq=13)
eyes_opened_alpha = eyes_opened.copy().filter(l_freq=8, h_freq=13)
eyes_closed_alpha.pick(['EEG PZ-A1_PZ-A1', 'EEG P3-A2_P3-A2', 'EEG P4-A1_P4-A1']).plot_psd(fmin=7, fmax=14)
eyes_opened_alpha.pick(['EEG PZ-A1_PZ-A1', 'EEG P3-A2_P3-A2', 'EEG P4-A1_P4-A1']).plot_psd(fmin=7, fmax=14)
"""

# ICA preprocessing segment

ica = mne.preprocessing.ICA(n_components=None, method='fastica', random_state=0)
ica.fit(eyes_closed)
ica.apply(eyes_closed)

plt.show()