from app import app
from flask import render_template

# views


@app.route("/")
def index():
    '''
    View Root Page Function that returns the index page and it's data
    '''
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template("index.html", title=title)


@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    '''
    View Movie Page that returns movie details page and it's data
    '''
    return render_template("movie.html", id=movie_id)
