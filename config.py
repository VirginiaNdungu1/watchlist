import os
'''
the os module allows applications to interact with the
operating system dependent functionality
'''


class Config:
    '''
    General Configuration Parent class
    Contains configurations used in both Production nad Devvelopment Stages
    '''
    MOVIE_API_BASE_URL = "https://api.themoviedb.org/3/movie/{}?api_key={}"
    SEARCH_MOVIE_URL = "https://api.themoviedb.org/3/search/movie?api_key={}&query={}"
    '''
    os.environ.get () function is used to get the MOVIE_API_KEY and the SECRET_KEY
    which we will set as environment variables
    '''
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production Configuration Child class
    Contains configurations in the Production Stages
    Inherits from the Parent Config class
    '''
    pass


class DevConfig(Config):
    '''
    Devvelopment Configuration Child class
    Contains configuration in the Devvelopment Stages
    Inherits from the Parent Config class
    Enable debug mode ij our applications
    '''
    DEBUG = True


# create a dictionary to help access the different configurations option classes
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
