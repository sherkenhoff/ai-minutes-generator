import subprocess

# Convert x seconds of a given audio file to ogg, saving at same filename with ogg extension
def convert_xs_of_audio_to_ogg(file_path, seconds):
    file_name = file_path.split('.')[0]
    new_file_path = f'{file_name}.ogg'
    subprocess.run(['ffmpeg.exe', '-i', file_path, '-t', str(seconds), new_file_path])

convert_xs_of_audio_to_ogg('audiofile.ext', 360)