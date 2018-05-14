import pandas as pd
from get_songs import get_songs
from get_lyrics import get_lyrics
from settings import CLIENT_ACCESS_TOKEN


HEADERS = {'Authorization': 'Bearer ' + CLIENT_ACCESS_TOKEN}
KENDRICK_LAMAR_ID = "1421"
KENDRICK_LAMAR = 'Kendrick Lamar'

songs = get_songs(HEADERS, KENDRICK_LAMAR_ID, max_songs=1)
lyrics = get_lyrics(songs, KENDRICK_LAMAR)


df = pd.DataFrame(lyrics)
df.to_csv('kendrick_lamar.csv')

print(df.head())
