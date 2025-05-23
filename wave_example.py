import wave

obj = wave.open("harvard.wav", "rb")

print("Number of channels: ", obj.getnchannels())
print("Sample width: ", obj.getsampwidth())
print("Frame rate: ", obj.getframerate())
print("Number of frames: ", obj.getnframes())
print("Parameters: ", obj.getparams())

time_audio = obj.getnframes()/ obj.getframerate()
print(time_audio)

frames = obj.readframes(-1) #read all frames
print(type(frames), type(frames[0]))
print(len(frames)/4) #(nchannels+samplewidth)= 2+2=4

obj.close()

obj_new=wave.open("harvard_new.wav","wb")

obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)

obj_new.writeframes(frames)

obj_new.close()