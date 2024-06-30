# pyaudio will give you a lot more low level control over how you play a sound
import pyaudio
import wave

filename = "sample-9s.wav"
chunk = 1024  # how many samples are put into each dataframe

# wavefile
wf = wave.open(filename, "rb")

# audio device
p = pyaudio.PyAudio()


stream = p.open(
    format=p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True, # sound will be played instead of getting recorded
)

data = wf.readframes(chunk)

while data!='':
    stream.write(data)
    data = wf.readframes(chunk)

stream.close()
p.terminate()
