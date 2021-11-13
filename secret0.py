# -*- coding: utf-8 -*-

import base64
import requests
client_id=""
client_secret=""



code_url="https://accounts.spotify.com/authorize"
method="GET"
code_data={
    "client_id":"",
    "response_type":"code",
    "redirect_uri":"https%3A%2F%2Fwww.google.com%2F",
    "scope":"playlist-modify-public"
}
client_cred=f"{client_id}:{client_secret}"
client_cred_b64=base64.b64encode(client_cred.encode())



token_url="https://accounts.spotify.com/api/token"
method="POST"
token_data={
    "grant_type":"refresh_token",
    "refresh_token":"",
    
}

token_header={
    "Authorization":f"Basic {client_cred_b64.decode()}"
}
r=requests.post(token_url,data=token_data,headers=token_header)
refresh=r.json()
refresh['access_token']

spotify_token=refresh['access_token']

spotify_user_id=""