#!C:/Users/user/AppData/Local/Programs/Python/Python310/python.exe
print()
import cgi
import requests
import pandas as pd
from request import *
form = cgi.FieldStorage()
playlist_name = form.getvalue("pass")


tracks_url = href[names.index(playlist_name)]
#requesting playlist items
s = requests.get(tracks_url + '/tracks' ,
                 headers=headers,
                 params={'market': 'IN'})

#Extracting song(track) names from the json output
e = s.json()
data_tracks = pd.DataFrame(e)
t_items = data_tracks['items']
track_items = dict(t_items)
song_list = []
for i in range(len(t_items)):
    track_tracks = track_items[i]
    track_track = track_tracks['track']
#    track_albums = track_track['album']
    track_name = track_track['name']
    song_list.append(track_name)
print(song_list)
"""
print('<html>')
for i in song_list:
    print('<p>'+i+'</p>')
print('</html>')
"""
