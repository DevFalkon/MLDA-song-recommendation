from flask import Flask, render_template, request, flash, redirect, url_for, session
import backend

app = Flask(__name__)
app.secret_key = "BAD_SECRET_KEY"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recom/<song_name>_by_<artist_name>")
def machine_learning(song_name, artist_name):
    recom = backend.get_recom(session['song_id'])
    return render_template("recom.html", song_name=song_name.title(), artist_name=artist_name.title(), results=recom)


@app.route("/", methods=["POST"])
def get_user_input():
    if request.method == "POST":
        song_name = request.form.get("song_name")
        artist_name = request.form.get("artist_name")
        if not song_name:
            flash("Song name can't be blank", "error")
        elif not artist_name:
            flash("Artist name can't be blank", "error")
        else:
            song_id = backend.get_song_id(song_name, artist_name)
            if song_id:
                session['song_id'] = song_id
                return redirect(url_for("machine_learning", song_name=song_name, artist_name=artist_name))
            else:
                flash(f"{song_name} by {artist_name} not in data set", "error")
        return render_template("index.html")
