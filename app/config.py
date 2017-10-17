class Config:
    '''
    General Configuration Parent class
    Contains configurations used in both Production nad Devvelopment Stages
    '''
    MOVIE_API_BASE_URL = "https: // api.themoviedb.org / 3 / movie / {}?api_key = {}"


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
