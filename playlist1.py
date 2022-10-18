#!C:/Users/user/AppData/Local/Programs/Python/Python310/python.exe
print()
import cgi
import requests
import pandas as pd
import pymysql
from request1 import *
import httplib2
import os
import sys
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser
from oauth2client.tools import run_flow
form = cgi.FieldStorage()
global playlist_name
global uid
#global playlist_name
playlist_name = form.getvalue("pass")
#playlist_name = "Ippude created"

def insert_playlist_name():
    connection = pymysql.connect(host='localhost',user='root',passwd='',database='mydatabase')
    cursor = connection.cursor()
    insert = "update project set playlistname='"+playlist_name+"' where uid='"+uid+"';"
    cursor.execute(insert)
    connection.commit()
    connection.close()

def select_playlist_name():
    connection = pymysql.connect(host='localhost',user='root',passwd='',database='mydatabase')
    cursor = connection.cursor()
    select = "select * from project;"
    cursor.execute(select)
    var = cursor.fetchone()
    playlist_name = var[1]
    connection.commit()
    connection.close()
    #print(playlist_name)
    return playlist_name
    
uid = selecting_uid()
names=request_names()
href=request_href()
#playlist_name = select_playlist_name()
def playlist():
    playlist_name = select_playlist_name()
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
    #print(song_list)
    return song_list



def get_authenticated_service():
    CLIENT_SECRETS_FILE = "client_secret_25404874492-3m7olm0ik49slf2efdsb9ll57735eddg.apps.googleusercontent.com.json"

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
#YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"
    yp = "https://www.googleapis.com/auth/youtubepartner"
    yfs = "https://www.googleapis.com/auth/youtube.force-ssl"
    yt = "https://www.googleapis.com/auth/youtube"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope={yp,yt,yfs},
    message=MISSING_CLIENT_SECRETS_MESSAGE)
    storage = Storage("client_secret_25404874492-3m7olm0ik49slf2efdsb9ll57735eddg.apps.googleusercontent.com-oauth2.json")
                      #% sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,http=credentials.authorize(httplib2.Http()))


def create_playlist(youtube,playlistName):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": playlistName
          },
          "status":{
            "privacyStatus": "public"  
          }
        }
    )
    response = request.execute()


if __name__=='__main__':
    insert_playlist_name()
    song_list = playlist()
    
    print('<!DOCTYPE html><html lang="en"><head><link type="text/css" rel="stylesheet" href="tracks_style.css"></head><body><form action="add.py"> <div class="heading"> <p class="head-text">Tracks</p></div><br><div class="container"> <ul>')
    for i in song_list:
        print('<li>'+'<p class="text">'+i+'</p>'+'</li>')
    print('</ul> </div><div><input type="submit" class="submit_btn" value="Add"></div></body></html>')
    youtube = get_authenticated_service()
    create_playlist(youtube,playlist_name)
    """
    print('<html>')
    for i in song_list:
        print('<p>'+i+'</p>')
    print('<form action="playlistid.py">')
    print('<input type="submit", value="Add">')
    print('</form>')
    print('</html>')
    """
