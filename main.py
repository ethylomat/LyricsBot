from flask import Flask, render_template
import os
from PyLyrics import *

app = Flask(__name__)

@app.route("/")
def hello():
    a=os.popen("./SpotifyControl/SpotifyControl info").read().split("\n")
    artist = a[1].replace(" Artist:   ", "")
    track = a[2].replace(" Track:    ", "")
    album = a[3].replace(" Album:    ", "")
    try:
        lyrics = PyLyrics.getLyrics(artist,track.replace("- Remastered", ""))
        pass
    except:
        lyrics = "No lyrics found"
        pass
    return render_template("index.html", artist = artist, track = track, album = album, lyrics = lyrics.replace("\n", "<br>"))
