import requests
import json
from dotenv import load_dotenv, find_dotenv
import os
from bs4 import BeautifulSoup
import pandas as pd

load_dotenv(find_dotenv())

CLIENT_ACCESS_TOKEN = os.getenv('CLIENT_ACCESS_TOKEN')
HEADERS = {'Authorization': 'Bearer ' + CLIENT_ACCESS_TOKEN}
KENDRICK_LAMAR_ID = "1421"
KENDRICK_LAMAR = 'Kendrick Lamar'


def parse_json(json_string):
    return json.dumps(json_string, indent=4)


def get_songs(headers, artist_id):
    page = 1
    all_songs = []
    url = "http://api.genius.com/artists/" + artist_id + "/songs"

    while True:
        payload = {'per_page': 50, 'page': page}
        result = requests.get(url, headers=headers, params=payload)
        json_result = json.loads(result.text)
        page_songs = json_result['response']['songs']
        next_page = json_result['response']['next_page']
        print('next page is: ' + str(next_page))
        if not isinstance(next_page, int):
            break
        page = next_page
        all_songs = all_songs + page_songs

    return all_songs


songs = get_songs(HEADERS, KENDRICK_LAMAR_ID)
lyrics = []

for song in songs:
    if song['primary_artist']['name'] == 'Kendrick Lamar':
        URL = 'https://genius.com' + song['path']
        page = requests.get(URL)
        html = BeautifulSoup(page.text, "html.parser")
        lyrics_string = html.find("div", class_="lyrics").get_text().encode('ascii', 'ignore')
        lyrics.append(lyrics_string)
        print(song['primary_artist']['name'] + ' - ' + song['full_title'] + ' - ' + str(song['id']))

df = pd.DataFrame(lyrics)
df.to_csv('kendrick_lamar.csv')

print(df.head())
