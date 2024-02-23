from exts import db
from datetime import datetime
from sqlalchemy.sql import func


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True , autoincrement=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)


class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100), nullable=False)


class SearchModel(db.Model):
    __tablename__ = "savedrecs"
    Authors = db.Column(db.String(255), primary_key=True,nullable=False)
    Author_Full_Names = db.Column(db.String(255), nullable=False)
    Article_Title = db.Column(db.String(255), primary_key=True,nullable=False)
    Document_Type = db.Column(db.String(255), nullable=False)
    Author_Keywords = db.Column(db.Text, nullable=False)
    Keywords_Plus = db.Column(db.String(255), nullable=False)
    Abstract = db.Column(db.Text, nullable=False)
    Email_Addresses = db.Column(db.String(255), nullable=False)
    Times_Cited_WoS_Core = db.Column(db.String(255), nullable=False)
    Times_Cited_All_Databases = db.Column(db.String(255), nullable=False)
    Publication_Year = db.Column(db.DateTime,default=func.now())
    Volume = db.Column(db.Integer)
    Issue = db.Column(db.Integer)
