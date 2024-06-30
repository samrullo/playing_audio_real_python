import sounddevice as sd
import soundfile as sf

filename = "sample-9s.wav"

# read data and sampling rate from the header of the wav file
data, fs = sf.read(filename,dtype='float32')

print(f"Start playing {filename}")
sd.play(data, fs)
status = sd.wait()
print(f"Finished playing {filename}")