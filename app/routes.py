from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'kkflyapple'}
    posts = [
        {
            'author': {'username': 'John Doe'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Sanny'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)