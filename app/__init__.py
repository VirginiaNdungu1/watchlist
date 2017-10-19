from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
# from config import DevConfig

bootstrap = Bootstrap()
# initialise the application


def create_app(config_name):
    app = Flask(__name__)
    # app = Flask(__name__, instance_relative_config=True)

    # creating app confiigurations
    app.config.from_object(config_options[config_name])

    # initialise flask extensions
    bootstrap.init_app(app)

    # register the Blueprint
    # import the Blueprint instance
    from .main import main as main_blueprint
    # call the register_blueprint() method on the application instance and pass in the Blueprint
    app.register_blueprint(main_blueprint)
    '''
    setting up config

    import configure_request function from requests module
    call the function and pass the application instance

    Reasons:
    We cannot access the application instance globally

    Solution:
    Therefore, we need to call the configure_request function
    when we create our application instance

    Benefits:
    Gives us access to the application objects
    '''

    from .request import configure_request
    configure_request(app)
    # We will add the views and forms

    return app


# setting up confiigurations
# app.config.from_object(DevConfig)
# app.config.from_pyfile("config.py")

# initialise Flask extensions
# bootstrap.init_app(app)
