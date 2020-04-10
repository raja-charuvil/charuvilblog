from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/image')
def image():
    return "Raja Asokan is a good boy!"
