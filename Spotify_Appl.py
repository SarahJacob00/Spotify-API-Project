from flask import Flask,render_template,request,redirect, url_for
from Playlist_meth import get_spotify_url,new_playlist,add_song_to_playlist
import json
import requests
from secret_spotify import username,pw
from browcheck import access_spotify



#ctrl+shift+R...i think


app= Flask(__name__,static_folder=r"C:\Users\jacob\Visual Studio\Spotify_Web\static")
i=0
all_song_info={}
imgs=''
add=0 # add=0(Nothing)  add=1(Yes)  add=2(No) add=3(Song invalid) add=4(No songs)
 

#PAGE FOR SUCCESSFUL CREATION AND REDIRECT TO SPOTIFY 
@app.route("/page3",methods = ['POST', 'GET'])
def page3():
   access_spotify(username,pw)
   return None

#PAGE TO CREATE PLAYLIST 
@app.route("/page2b",methods = ['POST', 'GET'])
def page2b():
    if request.method == 'POST': 
        name=request.form['pname']
        playlist_id=new_playlist(name)
        check=add_song_to_playlist(all_song_info,playlist_id)
        return render_template('page3.html',value=check)
    else: 
        name=request.args.get('pname')
        playlist_id=new_playlist(name)
        check=add_song_to_playlist(all_song_info,playlist_id)
        return render_template('page3.html',value=check)


#PAGE VERIFY SONG NOT FOUND
@app.route("/page2a",methods = ['POST', 'GET'])
def page2a():
    global add,i
    if request.method == 'POST': 
        if request.form['btn']=='Yes':
            add=1
            i=i+1
            #return "POST Yes"
        elif request.form['btn']=='No':
            add=2
            #return "POST No"
        return render_template('page1.html',value=add)
    else: 
        if request.args.get('btn')=='Yes':
            add=1
            i=i+1
            return render_template('page1.html',value=add)
        elif request.form('btn')=='No':
            add=2
            return render_template('page1.html',value=add)

#PAGE TO ADD SONGS
@app.route("/page1",methods = ['POST', 'GET'])
def page1():
    global i,add
    if request.method == 'POST':
        if request.form['done']=='Add':
            song = request.form['song']
            artist=request.form['artist']
            suri=get_spotify_url(song,artist)
            #return render_template('test.html',value1=song,value2=artist)
            if suri==0 or (song=='' and artist==''):
                add=3
                return render_template('page1.html',value=add) #Song Not found page

            s_name=suri['name']
            a_name=suri['album']['artists'][0]['name']
            imgs=suri['album']['images'][0]['url']

            all_song_info[i]={
                "song_name":s_name,
                "artist":a_name,
                "image":imgs,
                #add the uri,easy to get song to put into playlist
                "spotify_uri":suri['uri']
            }
            
            return render_template('page2a.html',image=imgs,song=s_name,artist=a_name) #Song VERIFIED page


        elif request.form['done']=='Done. Create Playlist!':
            if i==0:
                add=4
                return render_template('page1.html',value=add)
            else:
                #song_info2=set(all_song_info)
                return render_template('page2b.html',value=add,song_list=all_song_info)

        
    elif request.method=='GET':
        if request.form['done']=='Add':
            song = request.args.get('song')
            artist=request.args.get('artist')
            suri=get_spotify_url(song,artist)
            if suri==0:
                add=3
                return render_template('page1.html',value=add) #Song Not found page
            
            all_song_info[i]={
                "song_name":song,
                "artist":artist,
                #add the uri,easy to get song to put into playlist  
                "spotify_uri":suri
            }
            
            imgs=suri['album']['images'][0]['url']
            return render_template('page2a.html',image=imgs) #Song VERIFIED page


        elif request.form['done']=='Done. Create Playlist!':
            if i==0:
                add=4
                return render_template('page1.html',value=add)
            else:
                return render_template('page2b.html',value=add)
        

#HOME PAGE
@app.route("/home",methods = ['POST', 'GET'])
def home(): 
    global add
    if request.method == 'POST': 
      #user = request.form['nm'] 
      return render_template('page1.html',value=add)
    else: 
      #user = request.args.get('nm') 
      return render_template('page1.html',value=add)

@app.route("/")
@app.route("/routee",methods = ['POST', 'GET'])
def routee():
    if request.method == 'POST':
        return render_template('home.html')
    else:
        return render_template('home.html')

if __name__=='__main__':
    app.add_url_rule('/', 'routee', routee)
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/', 'page1', page1)
    app.add_url_rule('/', 'page2a', page2a)
    app.add_url_rule('/', 'page2b', page2b)
    
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)