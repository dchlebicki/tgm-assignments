import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , application.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'application.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('APPLICATION_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the current application context"""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request"""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database"""
    init_db()
    print('Initialized the database.')


@app.route('/')
def show_todolist():
    db = get_db()
    cur = db.execute('select id, title from todolist')
    entries = cur.fetchall()
    return render_template('show_todolist.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('insert into todolist (title) values (?)', [request.form['title']])
    db.commit()
    flash('New todo list item was successfully posted')
    return redirect(url_for('show_todolist'))