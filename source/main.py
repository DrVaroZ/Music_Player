# from music_player import MusicPlayer
from view_music_player import ViewMusicPlayer
# from control_music_player import ControlMusicPlayer
# import class from my package
from musicplayercontrolpackage.control_music_player import ControlMusicPlayer

player = ControlMusicPlayer()
gui = ViewMusicPlayer(player)
gui.run()
