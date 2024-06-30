import simpleaudio as sa
import numpy as np

freq = 440
fs = 44100
seconds = 3
t = np.linspace(0, 3, seconds * fs, False)
note = np.sin(2 * np.pi * t * freq)
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)
play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj.wait_done()
