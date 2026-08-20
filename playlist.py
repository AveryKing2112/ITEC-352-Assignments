# Avery King - 8/20/2026
# playlist.py (starter)
playlist = ["Here Comes the Sun", "Blue in Green", "All of Me"]

def add_song(title):
    # using mutation because we want to store in global veriable not local. 
    playlist.append(title)
    


def remove_song(title):
    # checks for a specific title in the global variable playlist
    if title in playlist:
        # remove the song title from the global variable playlist.
        playlist.remove(title)
        return True
    return False
    
    


def find_song(title):
    # checks for a specific song in the global playlist variable
    if title in playlist:
        # store the index in local variable position
        position = playlist.index(title)
        return(position)
    # same as false
    return -1
    

def get_playlist_copy():
    return playlist.copy()

def replace_song(old, new):
    """Replace first occurrence of old with new.
    Return (index, new) if replaced, else None.
    """
    idx = find_song(old)
    if idx == -1:
        return None
    playlist[idx] = new
    return (idx, new)

def main():
    print("Initial playlist:", playlist)
    add_song("Dream a Little Dream")
    print("After add:", playlist)
    removed = remove_song("All of Me")
    print("Removed 'All of Me'?", removed)
    print("Index of 'Blue in Green':", find_song("Blue in Green"))
    copy = get_playlist_copy()
    print("Copy:", copy)
    rep = replace_song("Here Comes the Sun", "Here Comes the Night")
    print("Replace result:", rep)
    print("Final playlist:", playlist)

if __name__ == "__main__":
    main()
