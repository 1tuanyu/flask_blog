from flask import Flask, render_template, g
import sqlite3
import os
app = Flask(__name__)

DATABASE = '/blog.db'

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def connect_db():
    rv = sqlite3.connect('blog.db')
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/home')
def home():
    cur = get_db().cursor()
    cur.execute('SELECT title, text FROM article')
    arts = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('home.html', arts=arts)


if __name__ == '__main__':
    app.run(debug=True)
