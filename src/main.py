import os
import random
from pynput import keyboard

from services.message_service import MessageService
from services.sound_services import SoundService 


BASE_PATH = os.path.join('./media', 'sounds')
AUDIO_LIST = ['audio1.wav', 'audio2.wav', 'audio3.wav', 
                'audio4.wav', 'audio5.wav']
CORRECT_AUDIO = 'correct.wav'
WRONG_AUDIO = 'wrong.wav'
WINNER_AUDIO = "winner.wav"


def shuffle_game(audio_list: list):
    new_audio_list = audio_list.copy()*2
    print(f"Antes: {new_audio_list}")
    random.shuffle(new_audio_list)
    
    return new_audio_list

def check_correctness(audio : str, position : int):
    
    if round_dict[1] == None:
        round_dict[1] = (audio, position)
        position_to_screen = (position, None)
        message = f"Reproduzindo audio na posição {position}: {audio}"
        MessageService.show_screen(completed, positions_played = position_to_screen, message=message)
        SoundService.play_sound(audio)
        
        
    elif round_dict[1][0] == audio and round_dict[1][1]!=position:
        completed[round_dict[1][1]] = 1
        completed[position] = 1
        position_to_screen = (round_dict[1][1], position)
        message = f"Reproduzindo audio na posição {position}: {audio}"
        MessageService.show_screen(completed, positions_played = position_to_screen, message=message)
        SoundService.play_sound(audio)
        SoundService.play_sound(CORRECT_AUDIO)
        round_dict[1] = None
        round_dict[2] = None
        position_to_screen = (None, None)
        
    else:
        position_to_screen = (round_dict[1][1], position)
        message = f"Reproduzindo audio na posição {position}: {audio}"
        MessageService.show_screen(completed, positions_played = position_to_screen, message=message)
        SoundService.play_sound(audio)
        SoundService.play_sound(WRONG_AUDIO)
        round_dict[1] = None
        round_dict[2] = None
        position_to_screen = (None, None)

        
    MessageService.show_screen(completed, positions_played = position_to_screen)

def on_press(key):

    MessageService.show_screen(completed)

    if key == keyboard.Key.esc:
            return False

    for i in range(10):

        if key == keyboard.KeyCode.from_char(str(i)):
            audio_to_play = new_audio_list[i]
            check_correctness(audio_to_play, i)

    if key.vk == 65437:
        audio_to_play = new_audio_list[5]
        check_correctness(audio_to_play, 5)


    if sum(completed) == len(completed):
        MessageService.show_screen(completed, message="Parabéns, voce concluiu o jogo")
        SoundService.play_sound(WINNER_AUDIO)
        return False        

def main():

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    new_audio_list = shuffle_game(AUDIO_LIST)
    completed = [0] * 10
    round_dict = {1: None, 2: None}
    
    MessageService.show_screen(completed)

    main()