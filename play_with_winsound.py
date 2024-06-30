import winsound

filename = "sample-9s.wav"

# only works for wav files
print(f"Start playing {filename}")
winsound.PlaySound(filename, winsound.SND_FILENAME)
print(f"finished playing {filename}")

# You can notify user something happened
print("Now will beep")
winsound.Beep(1000, 2000)
