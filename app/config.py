class Config:
    '''
    General Configuration Parent class
    Contains configurations used in both Production nad Devvelopment Stages
    '''
    pass


class ProdConfig(Config):
    '''
    Production Configuration Child class
    Contains configurations in the Production Stages
    Inherits from the Parent Config class
    '''
    pass:


class DevConfig(Config):
    '''
    Devvelopment Configuration Child class
    Contains configuration in the Devvelopment Stages
    Inherits from the Parent Config class
    Enable debug mode ij our applications
    '''
    DEBUG = True
