import mne
import matplotlib.pyplot as plt

# getting the raw data
raw_data = mne.io.read_raw_edf('./data/record.edf', preload=True)

# dropping bad channels
bad_channels = raw_data.ch_names[-5:-1]
bad_channels.append("SAO2-1")
preprocessed_data = raw_data.drop_channels(bad_channels)

# finding events
events = mne.events_from_annotations(preprocessed_data)
print(events)

#delta_freq_preprocessed_data = preprocessed_data.copy().filter(l_freq=0.5, h_freq=4)
#theta_freq_preprocessed_data = preprocessed_data.copy().filter(l_freq=4, h_freq=8)
#alpha_freq_preprocessed_data = preprocessed_data.copy().filter(l_freq=8, h_freq=13)
#beta_freq_preprocessed_data = preprocessed_data.copy().filter(l_freq=13, h_freq=30)
#gamma_freq_preprocessed_data = preprocessed_data.copy().filter(l_freq=30, h_freq=170)

# plotting eeg diagram
#gamma_freq_preprocessed_data.plot()
#beta_freq_preprocessed_data.plot()
#alpha_freq_preprocessed_data.plot()
#theta_freq_preprocessed_data.plot()
#delta_freq_preprocessed_data.plot()
#preprocessed_data.plot()
#plt.show()


#as

