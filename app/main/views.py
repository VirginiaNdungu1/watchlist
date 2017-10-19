from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_movies, get_movie, search_movie

from .forms import ReviewForm
from ..models import Reviews

# Reviews = review.Reviews
# views

# get movies view function


@main.route("/")
def index():
    '''
    View Root Page Function that returns the index page and it's data
    '''

    popular_movies = get_movies('popular')
    print(popular_movies)
    # latest_movies = get_movies('latest')
    # print(latest_movies)
    upcoming_movie = get_movies('upcoming')
    # print(upcoming_movie)
    now_showing_movie = get_movies('now_playing')
    # print(now_showing_movie)
    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('.search', movie_name=search_movie))
    else:
        return render_template("index.html", title=title, popular=popular_movies,  upcoming=upcoming_movie, now_showing=now_showing_movie)

# movie detail view function


@main.route("/movie/<int:id>")
def movie(id):
    '''
    View Movie Page that returns movie details page and it's data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'

    reviews = Reviews.get_reviews(movie.id)
    '''
    call the get_reviews class method in models/review.py file
    It takes in a movie ID
    returns a list of reviews for that movie
    pass the reviews list to our template
    '''
    return render_template("movie.html", title=title, movie=movie, reviews=reviews)

# search view Function


@main.route("/search/<movie_name>")
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f"search results for {{movie_name}}"
    return render_template("search.html", movies=searched_movies)
# review view function


@main.route("/movie/review/new/<int:id>", methods=['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    '''
    Create an instance of the ReviewForm Class
    '''
    movie = get_movie(id)
    '''
    call the get_movie() and pass in the id
    '''

    if form.validate_on_submit():
        '''
        validate_on_submit() method return True when
        form is submitted and all the data from the
        form input fields has been verified by validaters
        '''
        title = form.title.data
        review = form.review.data
        new_review = Reviews(movie.id, title, movie.image, review)
        new_review.save_review()
        return redirect(url_for('.movie', id=movie.id))
    title = f'{movie.title} review'
    return render_template('new_review.html', title=title, review_form=form, movie=movie)
