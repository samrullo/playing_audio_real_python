import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 5

print("Will start recording...")
myrecording = sd.rec(int(seconds*fs),samplerate=fs, channels=2)
sd.wait()
print("Finished recording ...")
write('output.wav', fs, myrecording)
print("Finished writing into output.wav")