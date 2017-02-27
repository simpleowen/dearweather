from init import db

class Weather(db.Model):
	"""weather table"""
	__tablename__ = 'weather'
	id = db.Column(db.Integer, primary_key=True)
	city = db.Column(db.String(10))
	weather_status = db.Column(db.String(10))
	tempreture = db.Column(db.Integer)
	tempreture_unit = db.Column(db.String(1)) 

	def __init__(self, city,weather_status,temp,temp_unit):
		self.city = city
		self.weather_status = weather_status
		self.tempreture = temp
		self.tempreture_unit = temp_unit

class History(db.Model):
	"""history table"""
	__tablename__ = 'history'

	id = db.Column(db.Integer, primary_key=True)
	city = db.Column(db.String(10))
	weather_status = db.Column(db.String(10))
	query_utc_time = db.Column(db.DateTime)
	client_ip = db.Column(db.String(20))
	tempreture = db.Column(db.Integer)
	tempreture_unit = db.Column(db.String(1))
	user_name = db.Column(db.String(20))

	def __init__(self, city,weather_status,query_utc_time,tempreture,tempreture_unit='C',client_ip=None,user_name='guest'):
		self.city = city
		self.weather_status = weather_status
		self.query_utc_time = query_utc_time
		self.tempreture = tempreture
		self.tempreture_unit = tempreture_unit
		self.client_ip = client_ip
		self.user_name = user_name

	