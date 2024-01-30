import tkinter as tk
from tkinter import ttk
from pygame import mixer
import youtube_dl
import ytm

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Music Player")
        self.root.geometry("400x300")

        self.playlist_url_entry = ttk.Entry(root, width=40)
        self.playlist_url_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.load_button = ttk.Button(root, text="Load Playlist", command=self.load_playlist)
        self.load_button.grid(row=0, column=3, padx=5, pady=10)

        self.play_button = ttk.Button(root, text="Play", command=self.play_music)
        self.play_button.grid(row=1, column=0, padx=10, pady=10)

        self.pause_button = ttk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.grid(row=1, column=1, padx=5, pady=10)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.grid(row=1, column=2, padx=5, pady=10)

        self.previous_button = ttk.Button(root, text="Previous", command=self.play_previous)
        self.previous_button.grid(row=1, column=3, padx=5, pady=10)

        self.next_button = ttk.Button(root, text="Next", command=self.play_next)
        self.next_button.grid(row=1, column=4, padx=5, pady=10)

        self.current_time_label = ttk.Label(root, text="0:00")
        self.current_time_label.grid(row=2, column=0, pady=10, columnspan=3)

        mixer.init()
        self.playlist = []
        self.current_song_index = 0

    def load_playlist(self):
        playlist_url = self.playlist_url_entry.get()
        self.playlist = self.get_playlist(playlist_url)
        self.current_song_index = 0

    def play_music(self):
        if self.playlist:
            current_song = self.playlist[self.current_song_index]
            mixer.music.load(current_song['url'])
            mixer.music.play()

    def pause_music(self):
        mixer.music.pause()

    def stop_music(self):
        mixer.music.stop()

    def play_previous(self):
        if self.current_song_index > 0:
            self.current_song_index -= 1
            self.play_music()

    def play_next(self):
        if self.current_song_index < len(self.playlist) - 1:
            self.current_song_index += 1
            self.play_music()

def get_playlist(self, playlist_url):
    playlist = []
    try:
        with youtube_dl.YoutubeDL({'quiet': True, 'extract_flat': True}) as ydl:
            result = ydl.extract_info(playlist_url, download=False)
            if 'entries' in result:
                for entry in result['entries']:
                    song_info = {
                        'title': entry['title'],
                        'url': entry['url'],
                    }
                    playlist.append(song_info)
        return playlist
    except Exception as e:
        print(f"Error loading playlist: {e}")
        return []
        playlist = []
        try:
            with youtube_dl.YoutubeDL({}) as ydl:
                result = ydl.extract_info(playlist_url, download=False)
                if 'entries' in result:
                    for entry in result['entries']:
                        song_info = {
                            'title': entry['title'],
                            'url': entry['url'],
                        }
                        playlist.append(song_info)
            return playlist
        except Exception as e:
            print(f"Error loading playlist: {e}")
            return []


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
