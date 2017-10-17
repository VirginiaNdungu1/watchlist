# import flask application instance
from app import app
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
import the movie module
'''
from models import movie

'''
get the api key from the config object
'''
api_key = app.config["MOVIE_API_KEY"]
'''
get the Movie Url from the config Object
'''
base_url = app.config["MOVIE_API_BASE_URL"]


def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(categoy, api_key)
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
        if get_movies_response["results"]:
            movie_results_list = get_movies_response["results"]
            movie_results = process_results(movie_results_list)
            '''
            if true:
            call the process_results(movie_results_list) function that takes in the list of dictionary objects and returns a list of movie Objects
            Assign it to a variable movie_results
            '''
        return movie_results

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
                title = movie_item.get("title")
                overview = movie_item.get("overview")
                image = movie_item.get("image")
                vote_average = movie_item.get("vote_average")
                vote_count = movie_item.get("vote_count")

                if image:
                    movie_object = Movie(
                        id, title, overview, image, vote_average, vote_count)
                    movie_results.append(movie_object)
            return movie_results
