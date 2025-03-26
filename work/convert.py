import pandas as pd
import unidecode

# Wczytanie pliku CSV
df = pd.read_csv('../data/spotify_tracks_fixed.csv')

# Funkcja usuwająca polskie znaki z tekstu
def remove_polish_chars(text):
    return unidecode.unidecode(text)

# Usuwanie polskich znaków z wybranych kolumn
df['Artist'] = df['Artist'].apply(remove_polish_chars)
df['Title'] = df['Title'].apply(remove_polish_chars)

# Zapisanie wyniku do nowego pliku CSV
df.to_csv('../data/a_no_polish.csv', index=False)
