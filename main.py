
from solution import *

with open('input.txt') as file:
    lines = file.readlines()
    song_1 = lines[0][:-1].split(',')
    song_2 = lines[1][:-1].split(',')
print('MENU OF YOUR MUSIC')
n = 1
for i in lines:
    print(str(n) + ' ' + str(i.split(',')[0]))
    n += 1
print(str(n + 1) + ' EXIT OF PROGRAM')
song = int(input('INPUT NUMBER OF TRACK: '))

while song != n+1:
    track = Playlist(lines[song - 1][:-1].split(','))
    print(track)
    print(track.play_music('on'))
    print(track.stop_music('off'))
    track.time_music_go()
    print(track.what_song())
    print(track.play_music('on'))
    track.time_music_go()
    track.time_music_go()
    track.time_music_go()
    track.time_music_go()
    print(track.now_time)
    track.del_song()
    song = int(input('INPUT NUMBER OF TRACK: '))


