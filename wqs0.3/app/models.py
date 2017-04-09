# coding:utf-8
from . import db


class Weather(db.Model):
	"""weather table"""
	__tablename__ = 'weather'
	id = db.Column(db.Integer, primary_key=True)
	city_name = db.Column(db.String(10))
	weather_status = db.Column(db.String(10))
	tempreture = db.Column(db.Integer)
	tempreture_unit = db.Column(db.String(1)) 

class History(db.Model):
	"""history table"""
	__tablename__ = 'history'
	id = db.Column(db.Integer, primary_key=True)
	city_name = db.Column(db.String(10))
	weather_status = db.Column(db.String(10))
	query_utc_datetime = db.Column(db.DateTime)
	client_ip = db.Column(db.String(20))
	tempreture = db.Column(db.Integer)
	tempreture_unit = db.Column(db.String(1))
	user_name = db.Column(db.String(20))