from flask import Flask ,render_template,request,redirect,url_for,jsonify,flash,session,logging,flash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

app=Flask(__name__)
app.secret_key="hello"


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os 


#home
@app.route('/')
def home ():
    return render_template('index.html')

#register form
@app.route("/register/")
def register():
    return render_template("register.html")

#login
@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"]=user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

#spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
	client_id=('ba07775d1854459d9bf4bb1f730055b5'),
	client_secret=('2c7a38bf64004c05ba1e81b0d4fb499d')
	)
)

@app.route('/posts',methods = ['POST', 'GET'])
def login9():
	if request.method == 'POST':
		search_text = request.form['nm']

		results = sp.search(q=search_text, limit=10)
		songlist = results['tracks']['items']

		return render_template('spotify-flask.html', tracks=songlist)
	else:
		user = request.args.get('nm')
		return render_template('spotify-flask.html')

if __name__ == "__main__":
    app.run(debug=True) 
