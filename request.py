#!C:/Users/user/AppData/Local/Programs/Python/Python310/python.exe
print()
import cgi
import requests
import pandas as pd
form = cgi.FieldStorage()

uid = form.getvalue("uid")
#playlist_name = form.getvalue("pass")
#Declaring variables and urls
#uid = "ucd9a5wrttcxjanjo8d85oeh7"
#playlist_name = "Project kosam"

CLIENT_ID = '68c40583d4f24203b2cf36bdcef93815'
CLIENT_SECRET = '37daffe5294145028854936c593e6aa1'
AUTH_URL = 'https://accounts.spotify.com/api/token'

#Auth
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


def request():
    #Declaring a base url
    BASE_URL = 'https://api.spotify.com/v1/'
    
    #requesting playlist names
    r = requests.get(BASE_URL + 'users/' + uid + '/playlists' ,
                     headers=headers,
                     params={'limit': 50, 'offset': 0})

    #Extracting playlist names from the json output
    d = r.json()
    names=[]
    href=[]
    data_playlist = pd.DataFrame(d)
    p_items = data_playlist['items']
    playlist_items = dict(p_items)
    for i in range(len(p_items)):
        all_items = dict(playlist_items[i])
        names.append(all_items['name'])
        href.append(all_items['href'])
        #print(all_items['name'])


    print('<html>')
    for i in names:
        print('<p>'+i+'</p>')
    print('<body><table width=100% height=100% border=1 bgcolor=orange><tr><td align=center>		<form enctype="multipart/form-data" action="playlist.py" method="get">		<table border=1 bgcolor=white>		<tr>			<td colspan=2 bgcolor=gray align=center>			<font color=white>Authentication</font>			</td>		</tr>                <tr>			<td>			Playlist name:			</td>			<td>			<input type="text" name="pass" />			</td>		</tr>   	        <tr>				<td colspan=2 align=center>			<input type="submit" name= "form" value="Submit" />			</td>		</tr>		</table>		</form></td></tr></table></body>')
    print('</html>')



#print(tracks_url)

#print(href)


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

"""
print("<html>")
for i in song_list:
    print("<p>",i,"</p>")
print("</html>")
"""
video_id = []
import urllib.request
import re
for i in song_list:
    #search_keyword=i
    #k=i.replace(" ","+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+i.replace(" ","+"))
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_id.append(video_ids[0])
#print(video_id)
#print(song_list)
import httplib2
import os
import sys
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser
from oauth2client.tools import run_flow


    # The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
    # the OAuth 2.0 information for this application, including its client_id and
    # client_secret. You can acquire an OAuth 2.0 client ID and client secret from
    # the Google Cloud Console at
    # https://cloud.google.com/console.
    # Please ensure that you have enabled the YouTube Data API for your project.
    # For more information about using OAuth2 to access the YouTube Data API, see:
    #   https://developers.google.com/youtube/v3/guides/authentication
    # For more information about the client_secrets.json file format, see:
    #   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets

CLIENT_SECRETS_FILE = "client_secret_821715650098-5tronmpkkt0qsk9rai2snroh7sqkf4c7.apps.googleusercontent.com.json"

    # This variable defines a message to display if the CLIENT_SECRETS_FILE is
    # missing.
MISSING_CLIENT_SECRETS_MESSAGE ="""
    

    WARNING: Please configure OAuth 2.0

    To make this sample run you will need to populate the client_secrets.json file
    found at:

    %s

    with information from the Cloud Console
    https://cloud.google.com/console

    For more information about the client_secrets.json file format, please visit:
    https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    """%os.path.abspath(os.path.join(os.path.dirname(__file__),
                               CLIENT_SECRETS_FILE))

    # This OAuth 2.0 access scope allows for full read/write access to the
    # authenticated user's account.
YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
#api_key = os.environ.get("YT_API_KEY")
#api_key = 'AIzaSyCzBwlTaKYBXW9XFmtx0cNE8AnCsGzZ5Is'
#youtube = build('youtube','v3',developerKey=api_key)

def get_authenticated_service():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)
    storage = Storage("client_secret_821715650098-5tronmpkkt0qsk9rai2snroh7sqkf4c7.apps.googleusercontent.com-oauth2.json")
                      #% sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,http=credentials.authorize(httplib2.Http()))

def add_video_to_playlist(youtube,videoID,playlistID):
    add_video_request=youtube.playlistItems().insert(
      part="snippet",
      body={
            'snippet': {
              'playlistId': playlistID, 
              'resourceId': {
                      'kind': 'youtube#video',
                  'videoId': videoID
                }
            #'position': 0
            }
    }
     ).execute()

if __name__ == '__main__':
    request()
    youtube = get_authenticated_service()
    for i in video_id:
        add_video_to_playlist(youtube,i,"PLbozq8BqgaQNJ6vcq_OmfkjIOT9cuIWW2")
"""
#Idhar se code ignore kar....
def ma():
    return song_list
def viewSongs():
    print('<html>')
    for i in song_list:
        print('<p>'+i+'</p>')
    print('<body bgcolor="skyblue"><p><form enctype="multipart/form-data" action="test.py" method="get"><input type="submit" value="Add" /></form></p></body>')
    print('</html>')
def printnames():
    print(names)
#if(__name__=='__main__'):
#    printnames()
#for i in song_list:
#    print("<option value='"+i+"'>"+i+"</option>")
#print("</select><input type=button value=Delete></center></form></body></html>")
"""
