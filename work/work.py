import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# spoti = pd.read_csv('spotify_tracks.csv')
# pd.set_option("display.max_columns", None)
# pd.set_option("display.expand_frame_repr", False)
#
#
# print(spoti.head(10))

df = pd.read_csv('../data/clean_lyrics.csv')
#
#
# # 🔹 Pobranie listy stop words (słów, które nie wnoszą wartości)
# nltk.download("stopwords")
# stop_words = set(stopwords.words("english"))
#
# # 🔹 Funkcja do czyszczenia tekstu
# def clean_lyrics(text):
#     if pd.isna(text):  # Sprawdza, czy tekst nie jest pusty
#         return ""
#
#     text = text.lower()  # Zamiana na małe litery
#     text = re.sub(r"\[.*?\]", "", text)
#     text = text.translate(str.maketrans("", "", string.punctuation))  # Usunięcie interpunkcji
#     words = text.split()  # Podział na słowa
#     words = [word for word in words if word not in stop_words]  # Usunięcie stop words
#     return " ".join(words)
#
# # 🔹 Czyszczenie tekstów w kolumnie "lyrics"
# df["clean_lyrics"] = df["tekst"].apply(clean_lyrics)
#
# # Podgląd wyników
# print(df[["tekst", "clean_lyrics"]].head())
# df[["clean_lyrics"]].to_csv("C:/Users/Kuba/Desktop/Projects/Music-data-analysis/clean_lyrics.csv", index=False)


# 🔹 Łączymy wszystkie słowa
text = " ".join(df['clean_lyrics'].dropna())

# 🔹 Tworzymy chmurę słów
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

# 🔹 Wyświetlamy chmurę słów
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
