#dependencies
#brew intall ffmpeg
#pip3 install pydub

from pydub import AudioSegment

audio = AudioSegment.from_wav("harvard.wav")

#increase the voulme by 6dB
audio = audio + 7

#repeat the clips
audio = audio * 2

#fade in
audio =  audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")