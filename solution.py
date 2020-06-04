class Load:
    """The class described """

    @classmethod
    def write(cls, file_input):
        with open(file_input) as file:
            cls.tracks = file.readlines()


class Playlist:
    """"""

    time_song = 0

    def __init__(self, song, play=False):
        """Initialization method."""
        self.title = song[0]
        self.time = song[1]
        self.name = song[2]
        self.album = song[3]
        self.year = song[4]
        self.play = play
        self.now_time = 0

    def play_music(self, new_command):
        """"""
        if new_command is not None:
            status_play = ''
            if new_command == 'play':
                self.play = True
                status_play = '"{}" play now.'.format(self.title)
            return status_play
        else:
            print('Error.')

    def stop_music(self, new_command):
        """"""
        if self.play is True:
            status_play = ''
            if new_command == 'stop':
                self.play = False
                status_play = '"{}" on pause.'.format(self.title)
            else:
                print('Error!')
            return status_play
        if self.play is False:
            print('You haven\'t turned on the music yet.')

    def what_song(self):
        """"""
        s = ''
        if self.play is True:
            s += f'"{self.title}"'
        else:
            s += 'Turned on the music yet.'
        return s

    def time_music(self):
        """"""
        pass
