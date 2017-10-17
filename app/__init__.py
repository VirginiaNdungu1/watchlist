from flask import Flask
from .config import DevConfig
# initialise the application

app = Flask(__name__, instance_relative_config=True)
# setting up confiigurations
app.config.from_object(DevConfig)
app.config.from_pyfile(config.py)


from app import views
