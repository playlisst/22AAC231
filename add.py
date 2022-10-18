#!C:/Users/user/AppData/Local/Programs/Python/Python310/python.exe
print()
import cgi
import requests
import pandas as pd
from request1 import *
from playlist1 import *
form = cgi.FieldStorage()

#playlistID = form.getvalue("playlistid")
#playlistID = "PL4Hwh0eiSARcssiwBkPshCV_ICeBN8heb"
#playlistID = "PLbozq8BqgaQOE4E7pHQe42Cz8uCzqchHk"
#playlistID = "PLh49ulWkF7ThLq3szm1gINq5V_cip4aU1"
song_list = playlist()
#print(song_list)
"""
names=request_names()
song_list = playlist()
href=request_href()
playlist_name=playlist_name()
"""
video_id = []
import urllib.request
import re
for i in song_list:
    #search_keyword=i
    #k=i.replace(" ","+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+i.replace(" ","+")+"+song")
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
YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
#api_key = os.environ.get("YT_API_KEY")
#api_key = 'AIzaSyCzBwlTaKYBXW9XFmtx0cNE8AnCsGzZ5Is'
#youtube = build('youtube','v3',developerKey=api_key)

def get_authenticated_service():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)
    storage = Storage("client_secret_25404874492-3m7olm0ik49slf2efdsb9ll57735eddg.apps.googleusercontent.com-oauth2.json")
                      #% sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,http=credentials.authorize(httplib2.Http()))

def get_list(youtube):
    request = youtube.playlists().list(
        part="snippet",
        channelId="UCrbwe_lFCcqQb1Pff5YwSMA"
    )
    response = request.execute()
    for i in response['items']:
        k=i['id']
        #print(i['snippet']['title'],"---",i['id'])
        break
    return k


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
    youtube = get_authenticated_service()
    playlistID = get_list(youtube)
    #print(playlistID)
    for i in video_id:
        add_video_to_playlist(youtube,i,playlistID)
    print('<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <link rel="stylesheet" href="end_page.css" type="text/css"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>End-page</title> </head> <body> <div class="pt-1"><p class="text">Your Playlist has been created.</p></div> <div class="pt-2"><p class="text">The link below will redirect you to it.</p></div> <a href="https://www.youtube.com/playlist?list='+playlistID+'"><div class = input_bar><p id="input-text" class="text">https://www.youtube.com/playlist?list=PLbozq8BqgaQOQ__VY1yFoaMnPkj44vx1F</p></div></a> <div class="pt-3"><p class="text">Follow the instructions to save it to your playlists.</p></div> <a href="link_instr.html" class="inst_link"><div class = "inst_bar"><p id="inst_text" class="text">Go to instructions</p></div></a> </body> </html>')
#    print('<h2>Added Successfully... The below link will redirect you to the youtube playlist...</h2>')
#    print('<h3><a href="https://www.youtube.com/playlist?list='+playlistID+'">Gimme mah playlist</a></h3>')
#    print('<h2>Use these instructions to get full access to your playlist</h2>')
#    print('<h4>...</h4>')
#    print('</html>')
    
    connection = pymysql.connect(host='localhost',user='root',passwd='',database='mydatabase')
    cursor = connection.cursor()
    insert = "truncate table project;"
    cursor.execute(insert)
    connection.commit()
    connection.close()
    
