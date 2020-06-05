import time


class Playlist:
    """This class describes the playlist"""

    time = ''

    def __init__(self, song, play=False):
        """Initialization method."""
        self.song = song
        self.title = song[0]
        self.time = song[1]
        self.name = song[2]
        self.album = song[3]
        self.year = song[4]
        self.play = play
        self.now_time = song[1]
        Playlist.time = song[1]

    def play_music(self, new_command):
        """Turn on the player."""
        if new_command is not None:
            status_play = ''
            if new_command == 'on':
                self.play = True
                status_play = 'Player on.'
            return status_play
        else:
            print('Error.')

    def stop_music(self, new_command):
        """Turn off the player."""
        if self.play is True:
            status_play = ''
            if new_command == 'off':
                self.play = False
                status_play = 'Player off.'
            else:
                print('Error!')
            return status_play
        if self.play is False:
            print('You haven\'t turned on.')

    def what_song(self):
        """Method that returns the song name."""
        s = ''
        if self.play is True:
            s += f'"{self.title}"'
        else:
            s += 'Turned on player.'
        return s

    def time_music_go(self):
        """Time of song."""
        if self.play is True:
            time_go = Playlist.timer(Playlist.time)
            time.sleep(1)
            time_go -= 1
            self.now_time = Playlist.timer(time_go)
            Playlist.time = self.now_time
            print(self.now_time)
        else:
            print('you didn\'t turn on the player.')

    def del_song(self):
        """Method for deleting a song."""

        del self.song

    @classmethod
    def timer(cls, time):
        """Converting time to seconds."""
        if isinstance(time, str):
            mint = time.split(':')[0]
            sec = time.split(':')[1]
            if mint == '00' and sec == '00':
                print('error')
                time = None
                return time
            else:
                if mint[0] == '0':
                    mint = int(mint[1])
                else:
                    mint = int(mint)
                if sec[0] == '0':
                    sec = int(sec[1])
                else:
                    sec = int(sec)
            result = mint*60 + sec
            return result

        if isinstance(time, int):
            n = 0
            time_ = time
            while time_ > 60:
                time_ -= 60
                n += 1
            mint = n
            sec = time - 60 * n
            if mint == 0:
                mint = '00'
            elif len(str(mint)) == 1:
                mint = '0' + str(mint)
            if sec == 0:
                sec = '00'
            if len(str(sec)) == 1:
                sec = '0' + str(sec)

            result = '{}:{}'.format(str(mint), str(sec))
            return result

    def __str__(self):
        """String method."""
        s = ''
        s += '**********_DOCUMENTATION LINE_**********' + '\n'
        s += f'TITLE: {self.title}' + '\n'
        s += f'BY {self.name} iN {self.year}' + '\n'
        s += f'ALBUM: {self.album}' + '\n'
        s += f'TIME: {self.time}' + '\n'
        s += f'________________________________________'

        return s

    def __repr__(self):
        return str(self.title)
