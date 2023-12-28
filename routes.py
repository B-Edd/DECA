import werkzeug
from flask import Blueprint, request, render_template, session, flash, redirect, url_for, current_app, \
    send_from_directory
from myapp import db, create_app
from .models import ShiftCalendar, Employee, Manager
# from .forms import ProductForm, lost_and_found_form
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
import os
from werkzeug.utils import secure_filename
import random
import json

bp = Blueprint('bp', __name__, static_folder='',
               static_url_path='/static')  # bp = Blueprint('bp', __name__, static_folder='static', static_url_path='/static')


@bp.route("/")
def index():
    # if session['existing_user_login.id']:
    # d = session['existing_user_login.id']
    # return redirect(url_for('bp.home', id=id))
    return render_template('index.html')


@bp.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        signup_username = request.form.get("signup-username")
        signup_email = request.form.get("signup-email")
        signup_password = request.form.get("signup-password")
        signup_employee_supervisor = request.form.get("signup-es")
        signup_manager_email = request.form.get("signup-manager-email")

        if signup_employee_supervisor == "supervisor":
            existing_username = Manager.query.filter_by(username=signup_username).first()
            existing_email = Manager.query.filter_by(email=signup_email).first()
            if existing_username or existing_email:
                flash("Username or email taken")
                return redirect(url_for('bp.index'))
            else:
                new_user = Manager(username=signup_username, password=signup_password, email=signup_email,
                                   employees_emails="")
                db.session.add(new_user)
                db.session.commit()
        elif signup_employee_supervisor == "employee":
            existing_username = Employee.query.filter_by(username=signup_username).first()
            existing_email = Employee.query.filter_by(email=signup_email).first()
            existing_manager_email = Manager.query.filter_by(email=signup_manager_email)
            if existing_username or existing_email:
                flash("Username or email taken")
                return redirect(url_for('bp.index'))
            else:
                new_user = Employee(username=signup_username, password=signup_password, email=signup_email,
                                    manager_email=signup_manager_email)
                db.session.add(new_user)
                db.session.commit()
    return redirect(url_for('bp.home'))


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_email = request.form.get("login-email")
        login_password = request.form.get("login-password")
        login_em = request.form.get("login-es")

        if login_em == 'login-supervisor':
            existing_user_login = Manager.query.filter_by(email=login_email).first()
            if existing_user_login and existing_user_login.check_password(login_password):
                session['existing_user_login.id'] = existing_user_login.id
                flash('Login successful!')
                session['logged_in'] = True
                return redirect(url_for('bp.home'))
            else:
                flash("Email or password wrong")
                return redirect(url_for('bp.index'))

        elif login_em == 'login-employee':
            existing_user_login = Employee.query.filter_by(email=login_email).first()
            if existing_user_login and existing_user_login.check_password(login_password):
                session['existing_user_login.id'] = existing_user_login.id
                flash('Login successful!')
                session['logged_in'] = True
                return redirect(url_for('bp.home'))
            else:
                flash("Email or password wrong")
                return redirect(url_for('bp.index'))
        else:
            flash("Employee or supervisor not checked")
            return redirect(url_for('bp.index'))

    return redirect(url_for('bp.home'))


@bp.route("/home")
def home():
    shifts = ShiftCalendar.query.all()
    return render_template('home/home.html', shifts=shifts)


@bp.route("/calendar")
def calendar():
    shifts = ShiftCalendar.query.all()
    return render_template('calendar/calendar.html', shifts=shifts)


@bp.route("/request-work-time-change")
def rwtc():
    shifts = ShiftCalendar.query.all()
    return render_template('request-work-time-change/rwtc.html', shifts=shifts)


@bp.route("/get_events")
def get_events():
    events = [
        {'title': 'Event 1', 'start': '2023-11-15'},
        {'title': 'Event 2', 'start': '2023-11-16'},
        {'id': 1, 'title': 'Event 21', 'start': '2023-11-01T10:00:00', 'end': '2023-11-01T12:00:00'},
    ]
    return json.dumps(events)
