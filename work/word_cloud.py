import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("../data/clean_lyrics.csv")

# 🔹 Łączymy wszystkie słowa
text = " ".join(df['clean_lyrics'].dropna())

# 🔹 Tworzymy chmurę słów
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

# 🔹 Wyświetlamy chmurę słów
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# # Zapisuję chmurę słów w /charts
# wordcloud.to_file("C:/Users/kk/PycharmProjects/music-data-analysis/charts/wordcloud.png")