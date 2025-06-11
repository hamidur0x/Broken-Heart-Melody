import time
import os
import sys
from threading import Thread
from playsound import playsound


timed_displays = [
    (4.93, "Is jawani me humne ye kya kar diya", 0.12),  
    (9.28, "Ishq me tere khud ko fana kar diya.", 0.12),  
    (14.37, "Mai to tujh me hi hu, tu na mujhme rha", 0.12), 
    (19.50, "Meri mosikiyon me tu Zinda rha..", 0.12), 
    (24.45, "", 0.12)
]
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_effect(text, custom_delay=0.05):
    sys.stdout.write("\t\t\t")  # Centering effect (tabs)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(custom_delay)
    print()  # Move to the next line after the phrase is typed

# Function to play audio in background
def play_audio(audio_file):
    playsound(audio_file)

def main():
    audio_path = "1.mp3"  # <-- Change to your audio filename or path

    # Start playing audio in a separate daemon thread
    audio_thread = Thread(target=play_audio, args=(audio_path,), daemon=True)
    audio_thread.start()

    # Start the timer
    start_time = time.time()

    # Initial clear to start with a clean screen
    clear_screen()
    print("\n\n")  # Add some initial newlines for spacing

    # Display the timestamps in sync with typing effect
    for entry in timed_displays:
        timestamp_trigger = entry[0]
        value_to_show = entry[1]
        delay = entry[2]

        # Wait until the specified timestamp is reached
        while time.time() - start_time < timestamp_trigger:
            time.sleep(0.01)  # Small sleep to avoid busy-waiting

        # Display the value with typing effect
        type_effect(value_to_show, delay)

if __name__ == "__main__":
    main()
