import sqlite3
from flask import Flask, g
app = Flask(__name__)

DATABASE = '/XieZhong.db'

def get_db():
    db = getattr(g,'_datebase', None)
    if db is None:
        db = g._datebase = sqlite3.connect(DATABASE)
        return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_datebase', None)
    if db is None:
        db.close()
