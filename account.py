from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Account(db.Model):

  user_id = db.Column(db.Integer, primary_key=True)
  account_number = db.Column(db.Integer, unique=True, nullable=False)
  pin = db.Column(db.Integer, nullable=False, unique=False)
  balance = db.Column(db.Integer, nullable=False, unique=False)
  name = db.Column(db.Text, unique=False)
  cc = db.Column(db.Text, unique=False)
  ccexp = db.Column(db.Integer, unique=False)
  cvv = db.Column(db.Integer, unique=False)