import pygame
import tkinter
import os
import webbrowser

from recommendation_model import RecommendationModel


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x750")
        pygame.init()
        pygame.mixer.init()
        self.find_song_var = tkinter.StringVar()
        self.recommend_music_var = tkinter.StringVar()

        title = tkinter.Label(self.root, text="Music Player", bd=5, relief=tkinter.GROOVE,
                              font=("times new roman", 20, "bold"), bg="white", fg="green")
        title.pack(side=tkinter.TOP, fill=tkinter.X)

        find_song_label = tkinter.Label(self.root, text="Enter track to find:", bg="white", fg="black")
        find_song_label.pack()
        self.find_song_entry = tkinter.Entry(self.root, textvariable=self.find_song_var, font=('calibre', 10, 'normal'))
        self.find_song_entry.pack()
        self.song_box = tkinter.Listbox(self.root, bg="white", fg="black", width=50)
        self.song_box.pack(pady=10)

        recommend_song_label = tkinter.Label(self.root, text="Enter your favourite tracks:", bg="white", fg="black")
        recommend_song_label.pack()
        self.recommend_music_entry = tkinter.Entry(self.root, textvariable=self.recommend_music_var, font=('calibre', 10
                                                                                                           , 'normal'))
        self.recommend_music_entry.pack()
        self.recommended_music_box = tkinter.Listbox(self.root, bg="white", fg="black", width=50)
        self.recommended_music_box.pack(pady=10)

        main_menu = tkinter.Menu(self.root)
        root.config(menu=main_menu)
        add_song_menu = tkinter.Menu(main_menu)
        main_menu.add_cascade(label='add song', menu=add_song_menu)
        add_song_menu.add_command(label='download song', command=self.download_song)
        add_song_menu.add_command(label='choose my songs', command=self.choose_song)

        play_button = tkinter.Button(self.root, text="Play Song", font=("Helvetica", 10), command=self.play)
        play_button.pack(pady=5)
        stop_button = tkinter.Button(self.root, text="Stop Song", font=("Helvetica", 10), command=self.stop)
        stop_button.pack(pady=5)
        find_button = tkinter.Button(self.root, text="Find Song", font=("Helvetica", 10), command=self.find_song)
        find_button.pack(pady=5)
        pause_button = tkinter.Button(self.root, text="Pause Song", font=("Helvetica", 10), command=self.pause)
        pause_button.pack(pady=5)
        unpause_button = tkinter.Button(self.root, text="Unpause Song", font=("Helvetica", 10), command=self.unpause)
        unpause_button.pack(pady=5)
        recommend_button = tkinter.Button(self.root, text="Recommend", font=("Helvetica", 10), command=self.recommend)
        recommend_button.pack(pady=5)

    def download_song(self):
        webbrowser.open("https://myfreemp3.fm/")

    def choose_song(self):
        '''
        songs = filedialog.askopenfilenames(initialdir='D:/Music/', title="Choose a song",
                                            filetypes=(("mp3 files", "*.mp3"),))

        for song in songs:
            song = song.replace("D:/Music/", "")
            song = song.replace(".mp3", "")
            song_box.insert(END, song)
        '''

        for song in os.listdir("D:/Music/"):
            song = song.replace(".mp3", "")
            self.song_box.insert('end', song)

    def find_song(self):
        song_to_find = self.find_song_entry.get()

        self.song_box.select_clear(first=0, last=tkinter.END)

        song_index = 0
        for song in self.song_box.get(0, tkinter.END):
            if song == song_to_find:
                self.song_box.select_set(first=song_index, last=song_index)
            song_index += 1

    def play(self):
        song = self.song_box.get(self.song_box.curselection())
        song = f'D:/Music/{song}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def recommend(self):
        favourite_music = self.recommend_music_entry.get()

        my_music = self.song_box.get(0, tkinter.END)
        model = RecommendationModel(my_music)
        result = model.recommend_music(favourite_music)

        for song in result.values:
            song_ = song[0]
            self.recommended_music_box.insert('end', song_)
