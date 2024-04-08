# STOPS OUTPUTTING SOUND AT 165 OR SO CHARACTERS (SOUNDS PLAYED, NOT KEYS PRESSED)
#I THINK IT'S A PLAYSOUND ISSUE WITH THE FILE HANDLING/LEAK

from playsound import playsound
import keyboard
# Define the base directory and file extension
# base_dir = './sounds/typewriter_sounds/new_names/'
base_dir = './sounds/animalese/'
file_ext = '.mp3'
# Function to generate file paths based on a pattern
def get_sound_file(key, shift_pressed=False):

    
    # Define the characters for each category
    lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number_chars = '0123456789'
    
    # Check if the key is a lowercase letter
    if key in lowercase_chars:
        # If Shift key is pressed, return the corresponding uppercase sound file
        if shift_pressed:
            return f"{base_dir}{key.upper()}{file_ext}"
        # Otherwise, return the lowercase sound file
        return f"{base_dir}{key.lower()}{file_ext}"
    
    # Check if the key is a number
    elif key in number_chars:
        return f"{base_dir}{key}{file_ext}"
    
    # If the key doesn't match any category, return the "other.mp3" sound file
    else:
        return f"{base_dir}other{file_ext}"

# Dictionary to keep track of whether a key is currently pressed down
key_down = {key: False for key in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'}
key_down['shift']=False

def play_sound(key):
    # print(key_down[key])
    if not key_down[key]:
        # print(key_down['shift'])
        key_down[key] = True
        print(f"playing sound {get_sound_file(key,shift_pressed=key_down['shift'])}... ")
        playsound(get_sound_file(key,shift_pressed=key_down['shift']), block=False)


def on_press(event):
    # print(event.name)
    # playsound(f"{base_dir}other{file_ext}", block=False)
    # return
    if event.name in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
        play_sound(event.name)
    else:
        if event.name == 'shift':
            # print("shift presed...")
            key_down['shift'] = True
        # playsound(f"{base_dir}other{file_ext}", block=False)


def on_release(event):
    # print(f"key released {event.name}")
    # if event.name in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
    key_down[event.name] = False

def on_action(event):
    if event.event_type == 'down':
        # print(f"{event.name} down")
        on_press(event=event)
    elif event.event_type == 'up':
        # print(f"{event.name} up")
        on_release(event=event)

# Capture key press and release events
keyboard.hook(on_action)

# Block the program until Ctrl+C is pressed
keyboard.wait('ctrl+c')
