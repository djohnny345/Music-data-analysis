import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download("punkt")
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

def preprocess(text):
    if isinstance(text, str):
        tokens = word_tokenize(text)  # Tokenizacja (podział na słowa)
        tokens = [word for word in tokens if word not in stop_words]  # Usunięcie stop words
        return tokens
    return []

df["Tokens"] = df["clean_lyrics"].apply(preprocess)

# Tworzenie słownika i korpusu dla LDA
dictionary = corpora.Dictionary(df["Tokens"])
corpus = [dictionary.doc2bow(text) for text in df["Tokens"]]

# Model LDA - wykrywanie tematów
lda_model = gensim.models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10)

# Wyświetlenie tematów
topics = lda_model.print_topics(num_words=10)
for topic in topics:
    print(topic)
