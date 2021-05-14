import random, os
from flask import Flask, render_template, request, session, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
ENV = 'dev'

@app.route('/')
def index():

    return render_template('index.html')

#FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB 
#FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB FBB 
@app.route("/fbb")
def fbb(): 
    if "fbb_user" in session:
        return render_template('z3_fbb.html')
    else:
        return redirect(url_for("fbb_login"))

@app.route("/fbb/login", methods = ["POST", "GET"])
def fbb_login():
    if request.method == "POST":
        fbb_user = request.form["fbb_user"]
        session['fbb_user'] = fbb_user

        return redirect(url_for("fbb_leaderboard", fbb_user=fbb_user)) #, fbb_team_name = fbb_team_name
    else:
        return render_template("z3_login.html")


if __name__ == '__main__':
    app.run()
