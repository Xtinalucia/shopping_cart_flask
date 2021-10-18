from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', name='you')


@app.route('/test')
def test():
    return render_template('test.html')