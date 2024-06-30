from pydub import AudioSegment

sound = AudioSegment.from_wav('output2.wav')

sound.export('output2_by_pydub.mp3', format="mp3")