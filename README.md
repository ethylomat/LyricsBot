# LyricsBot

LyricsBot is a local Flask app that finds the lyrics of the currently playing Spotify song

<table>
<tr>
<td>
<img src="https://static.ethylomat.de/img/lyricsbot.png" width="100%"><br>
<p align="center"><b>Lyrics: </b>http://127.0.0.1:5000/</p>
</td>
<td>
<img src="https://static.ethylomat.de/img/karaoke.png" width="100%"><br>
<p align="center"><b>Karaoke: </b>http://127.0.0.1:5000/karaoke</p>
</td>
</tr>
</table>

To run the LyricsBot you need to clone this repository rescursively.

```console
foo@bar:~$ git clone --recurse-submodules https://github.com/ethylomat/LyricsBot.git
Cloning into 'LyricsBot'...
remote: Counting objects: 139, done.
``` 


Start the app via the standard Flask-approach:
```console
foo@bar:~$ cd LyricsBot
foo@bar:~$ export FLASK_APP=main.py
foo@bar:~$ flask run
* Serving Flask app "main"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
``` 
