import pandas as pd
import matplotlib.pyplot as plt
spoti = pd.read_csv('../data/cleaned_tracks_lyrics.csv')
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)


print(spoti.head(10))


#
#

