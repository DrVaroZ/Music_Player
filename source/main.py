import os
from tkinter import *
# from tkinter import filedialog
import pygame
import webbrowser

root = Tk()
root.title('Music player')

root.geometry("500x400")

pygame.mixer.init()

find_song_var = StringVar()


def download_song():
    webbrowser.open("https://myfreemp3.fm/")


def choose_song():
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
        song_box.insert('end', song)


def find_song():
    song_to_find = find_song_entry.get()

    song_box.select_clear(first=0, last=END)

    song_index = 0
    for song in song_box.get(0, END):
        if song == song_to_find:
            song_box.select_set(first=song_index, last=song_index)
        song_index += 1


def play():
    song = song_box.get(song_box.curselection())
    song = f'D:/Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()


title = Label(root, text="Music Player", bd=5, relief=GROOVE,
              font=("times new roman", 20, "bold"), bg="white", fg="green")
title.pack(side=TOP, fill=X)

find_song_entry = Entry(root, textvariable=find_song_var, font=('calibre', 10, 'normal'))
find_song_entry.pack()

song_box = Listbox(root, bg="white", fg="black", width=50)
song_box.pack(pady=10)

main_menu = Menu(root)
root.config(menu=main_menu)
add_song_menu = Menu(main_menu)
main_menu.add_cascade(label='add song', menu=add_song_menu)
add_song_menu.add_command(label='download song', command=download_song)
add_song_menu.add_command(label='choose my songs', command=choose_song)

play_button = Button(root, text="Play Song", font=("Helvetica", 10), command=play)
play_button.pack(pady=5)
stop_button = Button(root, text="Stop Song", font=("Helvetica", 10), command=stop)
stop_button.pack(pady=5)
find_button = Button(root, text="Find Song", font=("Helvetica", 10), command=find_song)
find_button.pack(pady=5)

root.mainloop()
