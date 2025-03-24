import pandas as pd
import matplotlib.pyplot as plt
spoti = pd.read_csv('spotify_tracks.csv')
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)


print(spoti.head(10))


#
#

