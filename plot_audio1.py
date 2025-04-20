import wave
import matplotlib.pyplot as plt
import numpy as np

# Open WAV file
obj = wave.open("harvard.wav", "rb")

# Get properties
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
n_channels = obj.getnchannels()
sample_width = obj.getsampwidth()

# Read all frames
signal_wave = obj.readframes(n_samples)
obj.close()

# Calculate duration
time_audio = n_samples / sample_freq
print("Duration (s):", time_audio)

# Convert buffer to int16 numpy array
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# Reshape array to separate channels (shape: [samples, channels])
reshaped = signal_array.reshape(-1, n_channels)
left_channel = reshaped[:, 0]
right_channel = reshaped[:, 1]

# Create time array
times = np.linspace(0, time_audio, num=n_samples)

# Plot both channels
plt.figure(figsize=(15, 8))

plt.subplot(2, 1, 1)
plt.plot(times, left_channel)
plt.title("Left Channel")
plt.ylabel("Amplitude")
plt.xlabel("Time (s)")
plt.xlim(0, time_audio)

plt.subplot(2, 1, 2)
plt.plot(times, right_channel, color='orange')
plt.title("Right Channel")
plt.ylabel("Amplitude")
plt.xlabel("Time (s)")
plt.xlim(0, time_audio)

plt.tight_layout()
plt.show()
