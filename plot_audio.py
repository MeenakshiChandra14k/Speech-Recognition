import wave
import matplotlib.pyplot as plt
import numpy as np

# Open WAV file
obj = wave.open("harvard.wav", "rb")

# Get properties
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
n_channels = obj.getnchannels()

# Read frames and close file
signal_wave = obj.readframes(n_samples)
obj.close()

# Duration
time_audio = n_samples / sample_freq
print(time_audio)

# Convert to int16 array
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# If stereo, take one channel (left channel)
if n_channels == 2:
    signal_array = signal_array[::2]  # Take every second sample (left channel)

# Generate time axis
times = np.linspace(0, time_audio, num=signal_array.shape[0])

# Plot
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal (Left Channel)")
plt.ylabel("Signal amplitude")
plt.xlabel("Time (seconds)")
plt.xlim(0, time_audio)
plt.show()
