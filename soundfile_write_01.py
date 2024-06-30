import soundfile as sf

data, fs = sf.read("sample-9s.wav")

sf.write('sample-9s.flac', data, fs)