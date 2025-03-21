import pandas as pd
import lyricsgenius
import time

# Klucz API
API_KEY = 'HvUEBnzib78wk3We0zr0mMIwXCflfCCPwTZIhwo3Vr3B_gSl2aj4GO_oElrh4i1v'

# Tworzenie obiektu Genius
genius = lyricsgenius.Genius(API_KEY)

# Wczytanie pliku CSV ze Spotify
spotify_df = pd.read_csv('spotify_tracks.csv')

# Lista na wyniki
lyrics_data = []


# Funkcja do pobierania tekstu piosenki
def get_lyrics(artist, title):
    try:
        song = genius.search_song(title, artist)
        if song:
            return song.lyrics
        else:
            return None
    except Exception as e:
        print(f"Error while fetching lyrics for '{title}' by {artist}: {e}")
        return None


# Przejscie przez wszystkie piosenki w pliku CSV
for index, row in spotify_df.iterrows():
    artist = row['Artist']
    title = row['Title']
    print(f"Processing: {title} by {artist}")

    # Pobieranie tekstów piosenek
    lyrics = get_lyrics(artist, title)

    # Zapisywanie tekstów
    if lyrics:
        lyrics_data.append({
            'id': index + 1,
            'tekst': lyrics
        })
    else:
        print(f"No lyrics found for '{title}' by {artist}.")

    # Czekam żeby nie przekroczyć limitu API
    time.sleep(1)

# Tworzenie DataFrame z wynikami
lyrics_df = pd.DataFrame(lyrics_data)

# Zapis do pliku CSV
lyrics_df.to_csv('lyrics_output.csv', index=False)

print("Lyrics extraction complete. Results saved to 'lyrics_output.csv'.")
