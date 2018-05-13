import requests
import json
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

url = "http://api.genius.com/search?q=Kendrick%20Lamar"
CLIENT_ACCESS_TOKEN = os.getenv('CLIENT_ACCESS_TOKEN')
print(CLIENT_ACCESS_TOKEN)
headers = {'Authorization': 'Bearer ' + CLIENT_ACCESS_TOKEN}


result = requests.get(url, headers=headers)

parsed = json.loads(result.text)

print(json.dumps(parsed, indent=4))

hits = result.json()['response']['hits']


# for hit in hits:
#     print(hit['result']['title'])

# for hit in hits:
#     print(hit['result'])

