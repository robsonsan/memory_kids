import simpleaudio as sa
import os
import random
from pynput import keyboard


BASE_PATH = os.path.join('./media', 'sounds')
AUDIO_LIST = ['audio1.wav', 'audio2.wav', 'audio3.wav', 
                'audio4.wav', 'audio5.wav']
CORRECT_AUDIO = 'correct.wav'
WRONG_AUDIO = 'wrong.wav'


def shuffle_game(audio_list: list):
    new_audio_list = audio_list.copy()*2
    print(f"Antes: {new_audio_list}")
    random.shuffle(new_audio_list)
    
    return new_audio_list

def play_sound(audio : str):
    path = os.path.join('./media', 'sounds', audio)
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def check_correctness(audio : str, position : int):
    if round_dict[1] == None:
        round_dict[1] = (audio, position)
    elif round_dict[1][0] == audio:
        completed[round_dict[1][1]] = 1
        completed[position] = 1
        play_sound('correct.wav')
        round_dict[1] = None
    else:
        round_dict[1] = None
        play_sound('wrong.wav')
    message(completed)

def message(situation: str, message: str = ""):
    os.system('cls' if os.name=='nt' else 'clear')
    print("##################################################")
    print("#                   Jogo                         #")
    print("##################################################")
    print("#                  Situação                      #")
    print(f"               {situation}                          ")
    print(f"               {message}                        ")
    

def on_press(key):
   
    message(completed)

    if key == keyboard.Key.esc:
            return False

    if key.vk == 65437:
        audio_to_play = new_audio_list[5]

        message(completed, f"Executando audio: {audio_to_play}")

        play_sound(audio_to_play)
        check_correctness(audio_to_play, 5)
        
        return True
    
    for i in range(10):

        if key == keyboard.KeyCode.from_char(str(i)):
            audio_to_play = new_audio_list[i]
            message(completed, f"Executando audio: {audio_to_play}")
            play_sound(audio_to_play)
            check_correctness(audio_to_play, i)
            

def main():

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    new_audio_list = shuffle_game(AUDIO_LIST)
    completed = [0] * 10
    round_dict = {1: None, 2: None}
    
    message(completed)

    main()