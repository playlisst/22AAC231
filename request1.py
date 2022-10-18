#!C:/Users/user/AppData/Local/Programs/Python/Python310/python.exe
print()
import cgi
import requests
import pandas as pd
import pymysql
form = cgi.FieldStorage()
global uid
#uid = form.getvalue("uid")
uid = "ucd9a5wrttcxjanjo8d85oeh7"
#uid="34ohbhh862tahcbapkbha7a40"
def insert_uid():
    connection = pymysql.connect(host='localhost',user='root',passwd='',database='mydatabase')
    cursor = connection.cursor()
    insert = "insert into project (uid,playlistname) values ('"+uid+"','');"
    cursor.execute(insert)
    connection.commit()
    connection.close()

def selecting_uid():
    connection = pymysql.connect(host='localhost',user='root',passwd='',database='mydatabase')
    cursor = connection.cursor()
    select = "select * from project;"
    cursor.execute(select)
    var = cursor.fetchone()
    uid = var[0]
    connection.commit()
    connection.close()
    #print(uid)
    return uid

#uid = selecting_uid()

#playlist_name = form.getvalue("pass")
#Declaring variables and urls

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


def request_names():
    #Declaring a base url
    uid = selecting_uid()
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
    
    
    
    return names
    
def request_href():
    uid = selecting_uid()
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
    
    
    
    return href
    


#print(tracks_url)

#print(href)



if __name__ == '__main__':
    insert_uid()
    selecting_uid()
    names=request_names()
    cnt=1
    """   
    print('<!DOCTYPE html><html lang="en"><head> <link type="text/css" rel="stylesheet" ref="style.css"> </head><body> <div class="heading"> <p class="text">Available Playlists</p></div><br><div class="container"> <ul> <li> <input type="radio" id="f-option" name="selector"> <label for="f-option">Playlist-1</label> <div class="check"></div><div class="inside"></div></li><li> <input type="radio" id="s-option" name="selector"> <label for="s-option">Playlist-2</label> <div class="check"> <div class="inside"></div></div></li></ul> </div></body></html>')
    """
    
    print('<!DOCTYPE html><html lang="en"><head> <link type="text/css" rel="stylesheet" href="style.css"> </head><body><form enctype="multipart/form-data" action="playlist1.py" method="get"><div class="heading"> <p class="text">Available Playlists</p></div><br><div class="container"> <ul>')
    for i in names:
        print('<li>'+'<input type="radio" value="'+i+'" id="a'+str(cnt)+'" name="pass"><label for="a'+str(cnt)+'">'+i+'</label>'+'<div class="check"></div><div class="inside"></div></li>')
        cnt+=1
    print('</ul> </div><div class="submit"><input type="submit" class="submit_btn" value="Submit"></div></form></body></html>')
    




    """
    print('<!DOCTYPE html><html>')
    print('<h1>Select one playlist:</h1><body>')
    print('<form enctype="multipart/form-data" action="playlist1.py" method="get">')
    for i in names:
        print('<input type="radio" id="'+i+'" name="pass" value="'+i+'"><label for="'+i+'">'+i+'</label><br>')
    print('<input type="submit" name="form" value="Submit"></form></body></html>')
    """
    
    #print('<p>'+i+'</p>')
    #print('<body><table width=100% height=100% border=1 bgcolor=orange><tr><td align=center>		<form enctype="multipart/form-data" action="playlist1.py" method="get">		<table border=1 bgcolor=white>		<tr>			<td colspan=2 bgcolor=gray align=center>			<font color=white>Authentication</font>			</td>		</tr>                <tr>			<td>			Playlist name:			</td>			<td>			<input type="text" name="pass" />			</td>		</tr>   	        <tr>				<td colspan=2 align=center>			<input type="submit" name= "form" value="Submit" />			</td>		</tr>		</table>		</form></td></tr></table></body>')
    #print(x)

