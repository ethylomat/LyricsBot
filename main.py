from flask import Flask, render_template, request
import os, time
from PyLyrics import *

app = Flask(__name__)

def spotifyPlay():
    os.popen("./SpotifyControl/SpotifyControl play")
    pass

def spotifyPause():
    os.popen("./SpotifyControl/SpotifyControl pause")
    pass

def spotifyNext():
    os.popen("./SpotifyControl/SpotifyControl next")
    pass

def spotifyPrevious():
    os.popen("./SpotifyControl/SpotifyControl previous")
    pass

def spotifyInfo():
    infos = os.popen("./SpotifyControl/SpotifyControl info").read().split("\n")
    artist = infos[1].replace(" Artist:   ", "")
    track = infos[2].replace(" Track:    ", "")
    album = infos[3].replace(" Album:    ", "")
    try:
        lyrics = PyLyrics.getLyrics(artist,track.replace("- Remastered", ""))
        pass
    except:
        lyrics = "No lyrics found"
        pass
    return {"artist": artist, "track": track, "album": album, "lyrics": lyrics}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        command = request.form['command']
        if command == "next":
            spotifyNext()
        if command == "previous":
            spotifyPrevious()
        if command == "pause":
            spotifyPause()
        if command == "play":
            spotifyPlay()

        if command != "pause":
            time.sleep(0.2)
            info = spotifyInfo()
            return render_template("index.html", artist = info["artist"], track = info["track"], album = info["album"], lyrics = info["lyrics"].replace("\n", "<br>"))
        else:
            return render_template("info.html", info="Paused")

    if request.method == 'GET':
        info = spotifyInfo() 
        return render_template("index.html", artist = info["artist"], track = info["track"], album = info["album"], lyrics = info["lyrics"].replace("\n", "<br>"))

@app.route('/karaoke', methods=['GET', 'POST'])
def karaoke():
    if request.method == 'POST':
        command = request.form['command']
        if command == "next":
            spotifyNext()
        if command == "previous":
            spotifyPrevious()
        if command == "pause":
            spotifyPause()
        if command == "play":
            spotifyPlay()

        if command != "pause":
            time.sleep(0.2)
            
            info = spotifyInfo() 
            lines = [line for line in info["lyrics"].split("\n") if line != ""]
            lines.insert(len(lines), " ")
            lines.insert(0, " ")
            triples = [(lines[i-1], lines[i], lines[i+1]) for i in range(1, len(lines)-1)]
            lyrics = "\n".join(["<section data-background-image='static/img/background.png'><div class='prev'>%s</div><div class='main'>%s</div><div class='prev'>%s</div></section>" % (triple[0], triple[1], triple[2]) for triple in triples])
            return render_template("karaoke.html", artist = info["artist"], track = info["track"], album = info["album"], lyrics = lyrics)
        else:
            return render_template("karaoke.html", info="Paused")

    if request.method == 'GET':
        info = spotifyInfo() 
        lines = [line for line in info["lyrics"].split("\n") if line != ""]
        lines.insert(len(lines), "")
        lines.insert(0, "")
        triples = [(lines[i-1], lines[i], lines[i+1]) for i in range(1, len(lines)-1)]
        lyrics = "\n".join(["<section data-background-image='static/img/background.png'><div class='prev'>%s</div><div class='main'>%s</div><div class='prev'>%s</div></section>" % (triple[0], triple[1], triple[2]) for triple in triples])
        return render_template("karaoke.html", artist = info["artist"], track = info["track"], album = info["album"], lyrics = lyrics)

    

