# #  working api link gif
# 
# curl example "http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=YOUR_API_KEY&limit=5"


import requests
g_key = 'cJUfkaLFzT99VM58J07pVzSYhe98HtkU'

word_user = input('Enter the word')
# example
# word_user = 'rose'
from_api = requests.get(f'http://api.giphy.com/v1/gifs/search?q={word_user}&api_key={g_key}&limit=1')
link_gif = from_api.json()['data'][0]['url']
# print(from_api.json())
print(link_gif)