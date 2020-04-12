from app import app
from flask import render_template, url_for


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/books')
def books():
	return render_template('books.html')


@app.route('/images')
def images():
    return render_template('images.html')


@app.route('/articles')
def articles():
	return render_template('articles.html')


@app.route('/socialmedia')
def socialmedia():
	return render_template('socialmedia.html')


@app.route('/others')
def others():
	return render_template('others.html')
