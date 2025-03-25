# import pandas as pd
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud
#
# df = pd.read_csv("../data/clean_lyrics.csv")
#
# # 🔹 Łączymy wszystkie słowa
# text = " ".join(df['clean_lyrics'].dropna())
#
# # 🔹 Tworzymy chmurę słów
# wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
#
# # 🔹 Wyświetlamy chmurę słów
# plt.figure(figsize=(10,5))
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()
#
# # # Zapisuję chmurę słów w /charts
# # wordcloud.to_file("C:/Users/kk/PycharmProjects/music-data-analysis/charts/wordcloud.png")

#wordcloud dla rocka
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Załaduj dane z CSV
df = pd.read_csv("../data/cleaned_tracks_lyrics.csv")

# Filtruj dane, aby wybrać tylko utwory z gatunku "rock"
rock_lyrics = df[df['Genre'] == 'rock']['clean_lyrics']

# Połącz wszystkie teksty piosenek w jeden ciąg
rock_text = " ".join(rock_lyrics.dropna())

# Utwórz chmurę słów
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(rock_text)

# Wyświetl chmurę słów
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")  # Usuń osie
plt.title("Chmura słów dla gatunku 'Rock'", fontsize=16)
plt.show()