# from music_player import MusicPlayer
from view_music_player import ViewMusicPlayer
from control_music_player import ControlMusicPlayer
# import class from my package
# from musicplayercontrolpackage.control_music_player import ControlMusicPlayer
import pandas as pd
'''
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

gfile = drive.CreateFile({'id': '1l8RTojesib1KTuXZuhDwTXQQrl59ohGh'})
# Read file and set it as the content of this instance.
gfile.SetContentFile('D:/Python projects/Music_Player/recommendation_system'
                     '/spotify_genius_track_dataset/Data '
                     'Sources/useful_spotify_tracks.csv')
gfile.Upload()  # Upload the file.

download_file = drive.CreateFile({'id': '1l8RTojesib1KTuXZuhDwTXQQrl59ohGh'})
download_file.GetContentFile('D:/Python projects/Music_Player/recommendation_system'
                             '/spotify_genius_track_dataset/Data '
                             'Sources/useful_spotify_tracks.csv')

df = pd.read_csv('D:/Python projects/Music_Player/recommendation_system'
                 '/spotify_genius_track_dataset/Data '
                 'Sources/useful_spotify_tracks.csv')
print(df.head())
print(df.info())

'''


player = ControlMusicPlayer()
gui = ViewMusicPlayer(player)
gui.run()
