import sounddevice as sd
import wavio

fs = 44100
seconds = 5

print("Will start recording...")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
print("Finished recording ...")
# write('output.wav', fs, myrecording)
wavio.write("output3.wav", myrecording, fs, sampwidth=2)
print("Finished writing into output.wav")
