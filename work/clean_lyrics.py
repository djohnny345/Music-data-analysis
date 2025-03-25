import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 🔹 Pobranie listy stop words (słów, które nie wnoszą wartości)
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# 🔹 Funkcja do czyszczenia tekstu
def clean_lyrics(text):
    if pd.isna(text):  # Sprawdza, czy tekst nie jest pusty
        return ""

    text = text.lower()  # Zamiana na małe litery
    text = re.sub(r"\[.*?\]", "", text) # Usuwam oznaczenia w nawiasach ([refren], [zwrotka])
    text = text.translate(str.maketrans("", "", string.punctuation))  # Usunięcie interpunkcji
    words = text.split()  # Podział na słowa
    words = [word for word in words if word not in stop_words]  # Usunięcie stop words
    return " ".join(words)

# df_tracks = pd.read_csv("../data/spotify_tracks_with_id.csv")  # Plik z metadanymi piosenek
# df_lyrics = pd.read_csv("../data/lyrics_output.csv")  # Plik z tekstami piosenek
# df_lyrics.rename(columns={"id": "track_id"}, inplace=True)
# print(df_lyrics.head())
# df_combined = df_tracks.merge(df_lyrics, on="track_id", how="left")
# df_combined.to_csv("../data/combined_tracks_lyrics.csv", index=False)
# print("✅ Pliki połączone i zapisane jako combined_tracks_lyrics.csv")

# df = pd.read_csv("../data/combined_tracks_lyrics.csv")
# df["clean_lyrics"] = df["tekst"].apply(clean_lyrics)
# df.to_csv("../data/cleaned_tracks_lyrics.csv", index=False)
# df.drop(columns=["tekst"], inplace=True)
# df.to_csv("../data/cleaned_tracks_lyrics.csv", index=False)
# df = pd.read_csv('lyrics_output')
# # 🔹 Czyszczenie tekstów w kolumnie "lyrics"
# df["clean_lyrics"] = df["tekst"].apply(clean_lyrics)


