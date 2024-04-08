from pydub import AudioSegment
import os

def remove_initial_segment(input_path, output_path, duration_to_remove):
    audio = AudioSegment.from_file(input_path)
    audio_without_initial_segment = audio[duration_to_remove * 1000:]  # Convert duration to milliseconds
    audio_without_initial_segment.export(output_path, format="mp3")

def batch_remove_initial_segment(input_folder, output_folder, duration_to_remove):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for file in os.listdir(input_folder):
        if file.endswith(".mp3"):  # Assuming input files are in WAV format, modify if needed
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)
            remove_initial_segment(input_path, output_path, duration_to_remove)

# Adjust these paths and duration as per your requirements
input_folder = "./typewriter_sounds/new_names"
output_folder = "./animalese"
duration_to_remove = 0.025  # in seconds

batch_remove_initial_segment(input_folder, output_folder, duration_to_remove)

