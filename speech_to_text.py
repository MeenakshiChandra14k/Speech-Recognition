#dependency
#pip3 install assemblyai


import assemblyai as aai
from api_secrets import API_KEY_ASSEMBLYAI
aai.settings.api_key = API_KEY_ASSEMBLYAI

transcriber = aai.Transcriber()

audio_file = "output.wav"

# speaker label--- speaker diarization --- who is speaking
config = aai.TranscriptionConfig(speaker_labels=True)

transcript = transcriber.transcribe(audio_file, config)

if transcript.status == aai.TranscriptStatus.error:
    print(f"Transcription failed: {transcript.error}")
    exit(1)

print(f" \nFull Transcript: \n\n{transcript.text}")

print("\nSpeaker Segmentation:\n")

#each utterance contains speaker and text
for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker}: {utterance.text}")
