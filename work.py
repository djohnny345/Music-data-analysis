import pandas as pd
spoti = pd.read_csv('spotify_tracks.csv')
pd.set_option("display.max_columns", None)  # Pokazuje wszystkie kolumny
pd.set_option("display.expand_frame_repr", False)  # Zapobiega zwijaniu kolumn

# Wyświetlenie pierwszych 10 wierszy z pełnymi kolumnami
print(spoti.head(10))