import pygame.mixer
import keyboard

typewriter_mode = True

if typewriter_mode:
    base_dir = './sounds/typewriter_sounds/new_names/'
else:
    base_dir = './sounds/animalese/'
file_ext = '.mp3'

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

key_down = {key: False for key in f'{letters}{numbers}'}
key_down['shift']=False

pygame.mixer.init()

def play_sound(key):
    if key not in key_down:
        key_down[key]=False
    if not key_down[key]:
        key_down[key] = True
        sound = pygame.mixer.Sound(get_sound_file(key, shift_pressed=key_down['shift']))
        sound.play()

# Function to generate file paths based on a pattern
def get_sound_file(key, shift_pressed=False):
    if key in letters:
        if shift_pressed:
            return f"{base_dir}{key.upper()}{file_ext}"
        return f"{base_dir}{key.lower()}{file_ext}"
    
    elif key in numbers:
        return f"{base_dir}{key}{file_ext}"
    
    # If the key doesn't match any category, return the "other.mp3" sound file
    else:
        return f"{base_dir}other{file_ext}"

def on_press(event):
    if typewriter_mode or event.name in f'{letters}{numbers}':
        play_sound(event.name)
    if event.name == 'shift':
        key_down['shift'] = True

def on_release(event):
    key_down[event.name] = False

def on_action(event):
    if event.event_type == 'down':
        on_press(event=event)
    elif event.event_type == 'up':
        on_release(event=event)

keyboard.hook(on_action)
keyboard.wait('ctrl+c')
