import tkinter

import pygame


class ViewMusicPlayer:
    def __init__(self, player):
        self.player = player

        self.root = tkinter.Tk()
        self.root.title("Music Player")
        self.root.geometry("500x750")

        pygame.init()
        pygame.mixer.init()

        self.find_song_var = tkinter.StringVar()
        self.recommend_music_var = tkinter.StringVar()

        self.title = tkinter.Label(self.root, text="Music Player", bd=5, relief=tkinter.GROOVE,
                              font=("times new roman", 20, "bold"), bg="white", fg="green")
        self.title.pack(side=tkinter.TOP, fill=tkinter.X)

        self.find_song_label = tkinter.Label(self.root, text="Enter track to find:", bg="white", fg="black")
        self.find_song_label.pack()
        self.find_song_entry = tkinter.Entry(self.root, textvariable=self.find_song_var, font=('calibre', 10, 'normal'))
        self.find_song_entry.pack()
        self.song_box = tkinter.Listbox(self.root, bg="white", fg="black", width=50)
        self.song_box.pack(pady=10)

        self.recommend_song_label = tkinter.Label(self.root, text="Enter your favourite tracks:", bg="white", fg="black")
        self.recommend_song_label.pack()
        self.recommend_music_entry = tkinter.Entry(self.root, textvariable=self.recommend_music_var, font=('calibre', 10
                                                                                                           , 'normal'))
        self.recommend_music_entry.pack()
        self.recommended_music_box = tkinter.Listbox(self.root, bg="white", fg="black", width=50)
        self.recommended_music_box.pack(pady=10)

        self.main_menu = tkinter.Menu(self.root)
        self.root.config(menu=self.main_menu)
        self.add_song_menu = tkinter.Menu(self.main_menu)
        self.main_menu.add_cascade(label='add song', menu=self.add_song_menu)
        self.add_song_menu.add_command(label='download song', command=self.download)
        self.add_song_menu.add_command(label='choose my songs', command=self.choose_track)

        self.play_button = tkinter.Button(self.root, text="Play Song", font=("Helvetica", 10), command=self.play)
        self.play_button.pack(pady=5)
        self.stop_button = tkinter.Button(self.root, text="Stop Song", font=("Helvetica", 10), command=self.stop)
        self.stop_button.pack(pady=5)
        self.find_button = tkinter.Button(self.root, text="Find Song", font=("Helvetica", 10), command=self.find)
        self.find_button.pack(pady=5)
        self.pause_button = tkinter.Button(self.root, text="Pause Song", font=("Helvetica", 10), command=self.pause)
        self.pause_button.pack(pady=5)
        self.unpause_button = tkinter.Button(self.root, text="Unpause Song", font=("Helvetica", 10), command=self.unpause)
        self.unpause_button.pack(pady=5)
        self.recommend_button = tkinter.Button(self.root, text="Recommend", font=("Helvetica", 10), command=self.recommend)
        self.recommend_button.pack(pady=5)

    def download(self):
        self.player.download_song()

    def choose_track(self):
        songs = self.player.choose_song()
        for song in songs:
            self.song_box.insert('end', song)

    def play(self):
        song = self.song_box.get(self.song_box.curselection())
        song = f'D:/Music/{song}.mp3'
        self.player.play(song)

    def stop(self):
        self.player.stop()

    def find(self):
        song_to_find = self.find_song_entry.get()
        song_index = self.player.find_song(song_to_find)

        self.song_box.select_clear(first=0, last=tkinter.END)
        self.song_box.select_set(first=song_index, last=song_index)

    def pause(self):
        self.player.pause()

    def unpause(self):
        self.player.unpause()

    def recommend(self):
        favourite_music = self.recommend_music_entry.get()
        recommendations = self.player.recommend(favourite_music)

        self.recommended_music_box.delete(first=0, last=tkinter.END)

        for song in recommendations:
            # song_ = song[0]
            self.recommended_music_box.insert('end', song)

    def run(self):
        self.root.mainloop()
