import os
import json
import requests

from secret import spotify_user_id,spotify_token

user_id=spotify_user_id
s_token=spotify_token
all_song_info={}

def new_playlist(name):
        #name=input('What would you like to name your playlist:')
        request_body = json.dumps({
            "name": name,
            "description": "Spotify API Project",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(s_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json["id"]
    
    #Step 3 : Search For the song
    
def get_spotify_url(song_name,artist): #I REMOVED SELFFFF
        query="https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,artist)
        response=requests.get(query,
                             headers={
                                   "Content-Type":"application/json",
                                   "Authorization":"Bearer {}".format(spotify_token)  #self.s_token
                                   
                                   })
        
        response_json=response.json()
        #print(response_json)
        song=response_json['tracks']['items']
        #print(song)
        try:
            #url=song[0]['uri']
            url=song[0]
            return url
        except:
            #print('Song doesnt exist or spelt wrong...Try again')
            return 0

def add_song_to_playlist(all_song_info,playlist_id):   
        #collect all of url
        uris=[]
        for song,info in all_song_info.items():
            uris.append(info["spotify_uri"])
        
        #add all songs into new playlist
        request_data=json.dumps(uris)
        
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

        response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        # check for valid response status

        try:
            response_json = response.json()
            return 1  #PLAYLIST CREATED
        except:
            return 0 #NOT CREATED
        