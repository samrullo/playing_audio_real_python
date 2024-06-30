import soundfile as sf

filename="output.wav"

data,fs = sf.read(filename)

print(f"Will write {filename} as mp3 file")
sf.write("output.mp3", data, fs)