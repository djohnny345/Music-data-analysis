import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm  # 🔹 Pasek postępu

# 🔹 Konfiguracja
NUM_THREADS = 5  # Liczba wątków
SAVE_EVERY = 1000  # Zapis co X piosenek

# 🔹 Pobranie listy
df = pd.read_csv("../data/spotify_url.csv")
lyrics_data = []  # Lista wyników

# 🔹 Licznik pobranych piosenek
counter = 0

# 🔹 Lista User-Agentów
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
]

# 🔹 Funkcja pobierająca tekst piosenki (z obsługą błędów)
def get_lyrics(artist, title):
    base_url = "https://www.tekstowo.pl/piosenka,{artist},{title}.html"
    url = base_url.format(artist=artist.lower().replace(" ", "_"), title=title.lower().replace(" ", "_"))

    for attempt in range(3):  # 🔹 Max 3 próby
        try:
            headers = {"User-Agent": random.choice(USER_AGENTS)}
            response = requests.get(url, headers=headers, timeout=10)

            # 🔹 Obsługa błędu 429 (Too Many Requests)
            if response.status_code == 429:
                print("🚦 Za dużo zapytań! Czekam 60 sekund...")
                time.sleep(60)
                continue  # Spróbuj ponownie

            # 🔹 Jeśli strona nie zwróci kodu 200, zwróć brak tekstu
            if response.status_code != 200:
                print(f"⚠️ Błąd {response.status_code} dla {artist} - {title}")
                return None

            # 🔹 Parsowanie HTML
            soup = BeautifulSoup(response.text, "html.parser")
            lyrics_div = soup.find("div", class_="song-text")

            # 🔹 Obsługa pustego tekstu
            if not lyrics_div:
                print(f"⚠️ Brak tekstu dla {artist} - {title}, pomijam.")
                with open("missing_songs.txt", "a") as file:
                    file.write(f"{artist} - {title}\n")
                return None

            return lyrics_div.get_text(strip=True, separator=" ")

        except requests.exceptions.RequestException:
            print(f"⚠️ Problem z połączeniem, próba {attempt + 1}/3...")
            time.sleep(5)  # Czekamy 5 sek. i próbujemy ponownie

    print(f"❌ Nie udało się pobrać {artist} - {title}")
    return None


# 🔹 Funkcja dla wielowątkowości + licznik
def process_song(index, row):
    global counter  # 🔹 Modyfikujemy globalny licznik
    artist, title = row["Formatted_Artist"], row["Formatted_Title"]
    lyrics = get_lyrics(artist, title)

    if lyrics:
        lyrics_data.append({"Artist": artist, "Title": title, "Lyrics": lyrics})
        counter += 1  # 🔹 Aktualizacja licznika

    time.sleep(random.uniform(0.5, 1.5))  # 🔹 Losowa przerwa


# 🔹 Pasek postępu
with tqdm(total=len(df), desc="Pobieranie tekstów") as pbar:
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = {executor.submit(process_song, i, row): i for i, row in df.iterrows()}

        for future in futures:
            future.result()  # Czekamy na wynik
            pbar.update(1)  # 🔹 Aktualizacja paska
            print(f"\r📊 Pobrano: {counter}/{len(df)} piosenek", end="")  # 🔹 Dynamiczny licznik

            # 🔹 Zapisuj co 1000 piosenek
            if counter % SAVE_EVERY == 0:
                pd.DataFrame(lyrics_data).to_csv("../data/test.csv",
                                                 index=False)
                print(f"\n✅ Zapisano {counter} piosenek!")

# 🔹 Finalny zapis
pd.DataFrame(lyrics_data).to_csv("../data/test.csv", index=False)
print("\n✅ Pobieranie zakończone! Wszystkie dane zapisane.")