from flask import Flask
from .config import DevConfig
# initialise the application

app = Flask(__name__)
# setting up confiigurations
app.config.from_object(DevConfig)

from app import views
