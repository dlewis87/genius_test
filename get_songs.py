import requests
import json
import math


def get_songs(headers: object, artist_id: str, max_songs: int = 0) -> list:
    """
    :param headers: Auth Token
    :param artist_id: Genius Artist ID
    :param max_songs: Maximum number of songs to fetch
    :return: List of songs by artist
    """
    songs_per_page = 50
    max_page = math.ceil(max_songs / songs_per_page)

    url = "http://api.genius.com/artists/" + artist_id + "/songs"

    current_page = 1
    all_songs = []

    while max_page == 0 or current_page <= max_page:
        print('Current page is: ' + str(current_page))

        payload = {'per_page': songs_per_page, 'page': current_page}
        result = requests.get(url, headers=headers, params=payload)
        json_result = json.loads(result.text)['response']

        page_songs = json_result['songs']
        next_page = json_result['next_page']

        if not isinstance(next_page, int):
            break

        current_page = next_page
        all_songs = all_songs + page_songs

        if len(all_songs) >= max_songs:
            all_songs = all_songs[:10]
            break

    print(str(len(all_songs)) + ' songs fetched')
    return all_songs
