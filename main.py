import mne
import matplotlib
matplotlib.use('GTK4Agg')

import matplotlib.pyplot as plt

# getting the raw data
raw_data = mne.io.read_raw_edf('./data/record.edf', preload=True)

# dropping bad channels
bad_channels = raw_data.ch_names[-5:-1]
bad_channels.append("SAO2-1")
preprocessed_data = raw_data.drop_channels(bad_channels)

eyes_closed = preprocessed_data.copy().crop(tmin=146, tmax=161)
eyes_opened = preprocessed_data.copy().crop(tmin=168, tmax=180)

eyes_closed_alpha = eyes_closed.copy().filter(l_freq=8, h_freq=13)
eyes_opened_alpha = eyes_opened.copy().filter(l_freq=8, h_freq=13)

""" ica = mne.preprocessing.ICA(n_components=6, random_state=0)
    ica.fit(eyes_closed.filter(6, 35))
    ica.apply(eyes_closed)

    ica.plot_overlay(eyes_closed)
"""

eyes_closed_alpha.pick(['EEG PZ-A1_PZ-A1', 'EEG P3-A2_P3-A2', 'EEG P4-A1_P4-A1']).plot_psd(fmin=7, fmax=14)
eyes_opened_alpha.pick(['EEG PZ-A1_PZ-A1', 'EEG P3-A2_P3-A2', 'EEG P4-A1_P4-A1']).plot_psd(fmin=7, fmax=14)

plt.show()