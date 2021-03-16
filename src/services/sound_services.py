import simpleaudio as sa
import os

class SoundService:
    def __init__(self) -> None:
        pass

    @staticmethod
    def play_sound(audio : str):
        path = os.path.join('./media', 'sounds', audio)
        wave_obj = sa.WaveObject.from_wave_file(path)
        play_obj = wave_obj.play()
        play_obj.wait_done()