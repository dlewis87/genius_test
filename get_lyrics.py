import requests
from bs4 import BeautifulSoup


def get_lyrics(songs: list, artist: str = '') -> list:
    """
    :rtype: list
    :param songs: list of songs
    :param artist: artist name (for filtering main artists)
    :return:
    """
    all_lyrics = []
    for song in songs:
        primary_artist_name = song['primary_artist']['name']
        song_full_title = song['full_title']
        song_id = str(song['id'])
        url = 'https://genius.com' + song['path']

        if artist != '' and primary_artist_name == artist:
            page = requests.get(url)

            lyrics_string = get_lyrics_from_page(page)
            all_lyrics.append(lyrics_string)

            print(primary_artist_name + ' - ' + song_full_title + ' - ' + song_id)
    return all_lyrics


def get_lyrics_from_page(page) -> str:
    """
    :param page: page to scrape
    :return: string of lyrics
    """
    html = BeautifulSoup(page.text, "html.parser")
    lyrics_string = html.find("div", class_="lyrics").get_text()
    return lyrics_string
