# you might get warning saying couldn't find ffmpeg or avconv. when playing other types of audio files like mp3 you will need those
from pydub import AudioSegment
from pydub.playback import play

filename="sample-9s.wav"
#sound = AudioSegment.from_wav(filename)
sound = AudioSegment.from_mp3("sample-9s.mp3")
play(sound)

