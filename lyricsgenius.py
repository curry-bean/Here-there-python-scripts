import lyricsgenius

# Replace the value with your own Genius API access token
genius = lyricsgenius.Genius('P_8DtS6k9cwAggcK8TJL9jEn8hIBkWg94rYyERQ85YxzjnjS_LXIw1i3JCAzKaTj')

# Prompt the user to enter the song title and artist name
song_title = input('Enter the song title: ')
artist_name = input('Enter the artist name: ')

# Search for the lyrics of the song
song = genius.search_song(song_title, artist_name)

# Check if the song lyrics were found
if song is None:
    print(f"Sorry, lyrics for '{song_title}' by '{artist_name}' could not be found.")
else:
    # Print the lyrics
    print(song.lyrics)
