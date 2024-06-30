import simpleaudio as sa

filename="sample-9s.wav"
wave_obj = sa.WaveObject.from_wave_file(filename)
print(f"I will start playing {filename}")
play_obj = wave_obj.play()
play_obj.wait_done()
print(f"I am done playing {filename}")