from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(10280), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    manager_email = db.Column(db.String(502), unique=False, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, username, password, email, manager_email):
        self.username = username
        self.set_password(password)
        self.email = email
        self.manager_email = manager_email


class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(10280), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    employees_emails = db.Column(db.String(502), unique=False, nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, username, password, email, employees_emails):
        self.username = username
        self.set_password(password)
        self.email = email
        self.employees_emails = employees_emails


class ShiftCalendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    location = db.Column(db.String(2000), nullable=True)
    supervisor = db.Column(db.String(1000), nullable=True)
