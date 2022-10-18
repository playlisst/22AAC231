#!C:/Users/user/AppData/Local/Programs/Python/Python310/python.exe
print()
import cgi
import requests
import pandas as pd
from request1 import *
from playlist1 import *
form = cgi.FieldStorage()

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


print('<html>')
print('<body><table width=100% height=100% border=1 bgcolor=orange><tr><td align=center>		<form enctype="multipart/form-data" action="add.py" method="get">		<table border=1 bgcolor=white>		<tr>			<td colspan=2 bgcolor=gray align=center>			<font color=white>Enter Yt Playlist ID</font>			</td>		</tr>                <tr>			<td>			Playlist ID:			</td>			<td>			<input type="text" name="playlistid" />			</td>		</tr>   	        <tr>				<td colspan=2 align=center>			<input type="submit" name= "form" value="Submit" />			</td>		</tr>		</table>		</form></td></tr></table></body>')
#print('<p>'+playlist_name+'</p>')
print('</html>')

youtube = get_authenticated_service()


