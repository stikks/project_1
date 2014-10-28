from flask import Flask, g, redirect, render_template, url_for, request, session, flash
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from functools import wraps
#import sqlite3
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
import os
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
from models import *
#app.database = "quizzes.db"

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login to view page')
			return redirect(url_for('login'))
	return wrap

@app.route('/')
@login_required
def home():
	#g.db = connect_db()
	#cur = g.db.execute('select * from quizzes')
	#quizzes=[]
	#quizzes = [dict(name=row[0], about=row[1]) for row in cur.fetchall()] 
	#g.db.close()
	quizzes = db.session.query(QuizPost).all()
	return render_template('welcome.html', quizzes=quizzes,title='Home')

@app.route('/index')
def index():
	title = 'Quiz or Tease?'
	return render_template('index.html',title=title)


@app.route('/login', methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['password'] != 'admin':
			error = "Invalid password"
		else:
			session['logged_in'] = True
			flash('You were just logged in')
			return redirect(url_for('home'))
	title = 'Sign In'
	return render_template('login.html',title=title, error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were just logged out')
	return redirect(url_for('login'))

#def connect_db():
#	return sqlite3.connect(app.database)

if __name__ == '__main__':
	app.run()
