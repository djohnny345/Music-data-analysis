import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

# df_tracks = pd.read_csv("../data/spotify_tracks.csv")
# df_tracks["track_id"] = df_tracks.index  # Dodajemy ID na podstawie indeksu
# df_tracks.to_csv("../data/spotify_tracks_with_id.csv", index=False)



def get_sentiment(text):
    if isinstance(text, str):
        return TextBlob(text).sentiment.polarity  # Wynik od -1 (negatywny) do 1 (pozytywny)
    return None

df = pd.read_csv("../data/cleaned_tracks_lyrics.csv")
df["Sentiment"] = df["clean_lyrics"].apply(get_sentiment)
print(df[["clean_lyrics", "Sentiment"]].head())

sns.histplot(df["Sentiment"], bins=30, kde=True)
plt.title("Rozkład sentymentu tekstów piosenek")
plt.xlabel("Wartość sentymentu")
plt.ylabel("Liczba utworów")
plt.show()

df.groupby("Genre")["Sentiment"].mean().plot(kind="bar", figsize=(10,5))
plt.title("Średni sentyment w różnych gatunkach muzycznych")
plt.ylabel("Średni sentyment")
plt.savefig("../charts/sentiment_by_genre.png")
plt.show()

genres = df["Genre"].unique()  # Lista unikalnych gatunków

for genre in genres:
    plt.figure(figsize=(8, 4))
    subset = df[df["Genre"] == genre]  # Filtrujemy dany gatunek
    sns.histplot(subset["Sentiment"], bins=30, kde=True)
    plt.title(f"Rozkład sentymentu dla {genre}")
    plt.xlabel("Wartość sentymentu")
    plt.ylabel("Liczba utworów")
    plt.savefig(f"../charts/sentiment_{genre}.png")  # Zapis do pliku
    plt.show()