from song import Song
from collections import deque

def main():
    playlist = deque()
    working = True
    options = ['1', '2', '3', '4', '5']
    
    while working:
        print('''
            Options:
            1. Add a new song to the end of the playlist
            2. Insert a new song to the beginning of the playlist
            3. Play the next song
            4. Quit
            5. Display all songs
        ''')
        selection = input('Enter a selection: ')
        
        try:
            if selection not in options:
                raise ValueError("Not an option.")
            else:
                if selection == '1':
                    song = Song()
                    song.prompt()
                    playlist.append(song)
                elif selection == '2':
                    song = Song()
                    song.prompt()
                    playlist.appendleft(song)
                elif selection == '3':
                    try:
                        playing = playlist.popleft()
                        print('Playing song:')
                        playing.display()
                    except:
                        print('\nThe playlist is currently empty.')
                elif selection == '5':
                    print('\nPlaylist content:')
                    for item in playlist:
                        item.display()
                else:
                    working = False
                    print('\nGoodbye')
        except:
            print('Wrong option. Try one of the available options.')        
        
    
if __name__ == '__main__':
    main()