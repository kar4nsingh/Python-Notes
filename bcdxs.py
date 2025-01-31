import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        # Initialize pygame mixer
        pygame.mixer.init()

        # Variables
        self.current_file = None

        # UI Elements
        self.label = tk.Label(root, text="No file selected", font=("Arial", 12))
        self.label.pack(pady=20)

        self.play_button = tk.Button(root, text="Play", command=self.play_music, width=10)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music, width=10)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music, width=10)
        self.stop_button.pack(pady=5)

        self.open_button = tk.Button(root, text="Open File", command=self.open_file, width=10)
        self.open_button.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.current_file = file_path
            self.label.config(text=f"Loaded: {file_path.split('/')[-1]}")

    def play_music(self):
        if self.current_file:
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()
        else:
            self.label.config(text="No file loaded!")

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
