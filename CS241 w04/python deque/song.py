class Song:
    def __ini__(self):
        self.title = title
        self.artist = artist
    def prompt(self):
        self.title = input('Enter the title: ')
        self.artist = input('Enter the artist: ')
    def display(self):
        print('{} by {}'.format(self.title, self.artist))