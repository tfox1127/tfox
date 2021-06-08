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

if __name__ == '__main__':
    app.run()
