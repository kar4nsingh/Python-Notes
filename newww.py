import pygame
from tkinter import*
from tkinter import filedialog


    
root = Tk()
root.title("Music Player")
root.geometry("400x200")
root.resizable(False, False)

current_file = None
pygame.mixer.init()

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    # if file_path:
    #     label.config(text=f"Loaded: {file_path.split('/')[-1]}")

def play_music():
        if current_file:
            current_file = open_file
            pygame.mixer.music.load(current_file)
            pygame.mixer.music.play()
        else:
            label.config(text="No file loaded!")

def pause_music():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

def stop_music():
        pygame.mixer.music.stop()

        # UI Elements
label = Label(root, text="No file selected", font=("Arial", 12))
label.pack(pady=20)

    
play_button = Button(root, text="Play", command=play_music, width=10)
 
play_button.pack(pady=5)
pause_button = Button(root, text="Pause", command=pause_music, width=10)
    
pause_button.pack(pady=5)
stop_button = Button(root, text="Stop", command=stop_music, width=10)
    
stop_button.pack(pady=5)
open_button = Button(root, text="Open File", command=open_file, width=10)
    
open_button.pack(pady=10)

root.mainloop()
