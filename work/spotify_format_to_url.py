import pandas as pd
import re
import unicodedata

# Wczytaj plik CSV
df = pd.read_csv("../data/a_no_polish.csv")

# Funkcja do konwersji tekstu
def format_text(text):
    text = text.lower()  # Małe litery
    text = re.sub(r"[^\w\s]", "", text)  # Usunięcie znaków specjalnych
    text = re.sub(r"\s+", "_", text)  # Zamiana spacji na "_"
    return text

# Tworzenie nowych kolumn
df["Formatted_Artist"] = df["Artist"].astype(str).apply(format_text)
df["Formatted_Title"] = df["Title"].astype(str).apply(format_text)

# Zapis do pliku
df.to_csv("../data/spotify_url.csv", index=False)

print("Plik spotify_url.csv został zapisany!")
