import requests
import base64
import pandas as pd
import time
import os

# Dane Spotify API
CLIENT_ID = "91272f62712a4549930adfe117ce9ac9"
CLIENT_SECRET = "b3fcf3941313415ebcaef8cd43930e28"

# Pobranie tokena autoryzacyjnego
def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("❌ Błąd autoryzacji!", response.text)
        return None

# Pobranie utworów dla podanego roku i gatunku
def get_tracks(year, genre, access_token, limit=50, max_tracks=1000):
    all_tracks = []
    offset = 0

    while len(all_tracks) < max_tracks:
        url = f"https://api.spotify.com/v1/search?q=year:{year} genre:{genre}&type=track&limit={limit}&offset={offset}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            tracks = response.json()["tracks"]["items"]

            print(f"📊 Wyniki dla {genre} {year}: {len(tracks)} utworów")

            if not tracks:
                break  # Koniec dostępnych utworów

            all_tracks.extend([
                (track["name"], track["artists"][0]["name"], year, genre, track["popularity"])
                for track in tracks
            ])

            offset += limit  # Przesunięcie dla kolejnej strony wyników
            time.sleep(0.5)  # Uniknięcie blokady API
        else:
            print(f"❌ Błąd pobierania dla {genre} {year}: {response.text}")
            break

    return all_tracks

# Pobranie i zapisanie danych do CSV
def get_all_tracks(start_year, end_year, genres, filename="spotify_tracks_fixed.csv"):
    access_token = get_access_token()
    if not access_token:
        print("❌ Nie udało się uzyskać tokena. Zakończono.")
        return

    all_tracks = []

    for year in range(start_year, end_year + 1):
        for genre in genres:
            print(f"📥 Pobieram {genre} z roku {year}...")
            tracks = get_tracks(year, genre, access_token, max_tracks=1000)

            if tracks:
                all_tracks.extend(tracks)
            else:
                print(f"⚠️ Brak wyników dla {genre} {year}")

    if all_tracks:
        df = pd.DataFrame(all_tracks, columns=["Title", "Artist", "Year", "Genre", "Popularity"])

        # Dopisywanie do istniejącego pliku zamiast nadpisywania
        df.to_csv(filename, mode="a", index=False, encoding="utf-8-sig", header=not os.path.exists(filename))
        print(f"✅ Dodano {len(all_tracks)} utworów do {filename}")

# Pobranie danych dla kilku gatunków
get_all_tracks(2020, 2020, ["rock", "pop", "rap"])
