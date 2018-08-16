from flask import Flask, render_template, request
from pubsub import pub
from space_weather_service.controller import Controller
#from space_weather_service.forms import ConfigForm


space_weather_service = Flask(__name__)
#space_weather_service.config.from_object("config")

controller = Controller()


@space_weather_service.route('/')
def index():
    return render_template('base.html', title='Service')
