from solution import *

with open('input.txt') as file:
    lines = file.readlines()
    #print('|     *MENU_OF_YOUR_PLAYLIST*\n| play - if you want to play a song\n| stop - if you want to stop the song\n'
    #     '| next - if you want to listen to the next one\n| end - if you want to finish')
    #answer = str(input())
    fix = 0
song = lines[0][:-1].split(',')
track = Playlist(song)
print(track.play_music('play'))
print(track.stop_music('stop'))
print(track.what_song())
print(track.play_music('play'))
print(track.what_song())



