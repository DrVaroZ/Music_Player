import os
import webbrowser
import pygame

from recommendation_model import RecommendationModel


class ControlMusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []

    def download_song(self):
        webbrowser.open("https://myfreemp3.fm/")

    def choose_song(self):
        for song in os.listdir("D:/Music/"):
            song = song.replace(".mp3", "")
            self.playlist.append(song)

        return self.playlist

    def find_song(self, song):
        track_to_find = song

        song_index = 0
        for track in self.playlist:
            if track == track_to_find:
                break
            song_index += 1

        return song_index

    def play(self, selected_song):
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play(loops=0)

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def recommend(self, favourites):
        favourite_music = favourites

        # my_music = self.song_box.get(0, tkinter.END)
        my_music = self.playlist
        model = RecommendationModel(my_music)
        result = model.recommend_music(favourite_music)

        return result
