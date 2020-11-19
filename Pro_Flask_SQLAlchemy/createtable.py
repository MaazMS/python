from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICTIONS'] = False
db = SQLAlchemy(app)


class GithubRepo(db.Model):
    roll_number = db.Column(db.Integer, primary_key=True)
    std_name = db.Column(db.String(80),  nullable=False)
    attendance = db.Column(db.DateTime, default=datetime.utcnow)