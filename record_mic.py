#dependencies
#brew install portaudio
#pip install pyaudio

import pyaudio
import wave

FRAMES_PER_BUFFER = 3200 #the number of audio samples per read
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000 # samples per second

#pyaudio object
p = pyaudio.PyAudio()

#open a stream to record
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("Start recording")

seconds = 5
frames = []

# RATE/FRAMES_PER_BUFFER*seconds ---- number of chunks
for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data =  stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav", "wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()