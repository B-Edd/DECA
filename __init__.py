from flask import Flask, request, jsonify, render_template, session, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
import os
from werkzeug.utils import secure_filename
import random


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_url_path='/static')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Eddie:Denisdailyvxwx1!@localhost/workscheduler'
    app.secret_key = "Sq88;&3’m"

    from .routes import bp  # Assuming you have a 'routes.py' file
    app.register_blueprint(bp)

    from .models import db
    db.init_app(app)
    return app


# flask run --host=0.0.0.0   run on all devices
'''@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'''
