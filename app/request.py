# import flask application instance
# from app import app

'''
urllib.request makes a connection to our API url
And sends a request
'''
import urllib.request
'''
json formats the JSON response to a python dictionary
'''
import json
'''
import the Movie class
'''
from .models import Movie
# Movie = movie.Movie
# get the api key
api_key = None
#  get the movie base url
base_url = None
# get the movie search url
search_url = None


def configure_request(app):
    '''
    Function that takes in the application instance
    And Replaces the values of the None variables
    to application configuration objects
    '''
    global api_key, base_url, search_url

    api_key = app.config['MOVIE_API_KEY']
    '''
    get the api key from the config object
    '''

    base_url = app.config['MOVIE_API_BASE_URL']
    '''
    get the Movie Url from the config Object
    '''

    search_url = app.config['SEARCH_MOVIE_URL']
    '''
    get the Search Movie Url from the config Object
    '''


def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category, api_key)
    '''
    .format() method takes in the parameters and repplaces them with the {} placeholder in the base_url
    Creates the get_movies_url as the final URL for our API request
    '''
    with urllib.request.urlopen(get_movies_url) as url:
        '''
        urllib.request.urlopen() function opens the url that is passed inside it
        In this case, the get_movies_url
        '''
        get_movies_data = url.read()
        '''
        .read() function to read the response
        define a variable get_movies_data and assign it to result of .read()
        '''
        get_movies_response = json.loads(get_movies_data)
        '''
        json.loads() function converts the JSON response
        to a python dictionary
        '''
        movie_results = None
        # check if response has any results
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)
            '''
            if true:
            call the process_results(movie_results_list) function that takes in the list of dictionary objects and returns a list of movie Objects
            Assign it to a variable movie_results
            '''

    return movie_results


def get_movie(id):
    get_movie_details_url = base_url.format(id, api_key)
    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            image = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id, title, overview, image,
                                 vote_average, vote_count)

    return movie_object


def search_movie(movie_name):
    search_movie_details_url = search_url.format(api_key, movie_name)
    with urllib.request.urlopen(search_movie_details_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results


def process_results(movie_list):
    '''
    Function that processes the movie result and transform them to a list of Objects

    Args:
    movie_list: a list of dictionaries that contain movie details

    Returns:
    movie_results: A list of movie Objects
    '''
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get("id")
        title = movie_item.get("original_title")
        overview = movie_item.get("overview")
        poster = movie_item.get("poster_path")
        vote_average = movie_item.get("vote_average")
        vote_count = movie_item.get("vote_count")

        if poster:
            movie_object = Movie(id, title, overview, poster,
                                 vote_average, vote_count)
            movie_results.append(movie_object)
    return movie_results
