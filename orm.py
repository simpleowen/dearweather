# coding:utf-8
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

class CRUD(object):
	"""docstring for ClassName"""
	def __init__(self,weather=None):
		self.weather = weather

	def save_to_db(self):
		"""insert or update a record"""
		a_history = History(self.weather['city_name'],self.weather['status'],\
			self.weather['query_utc_datetime'],int(self.weather['tempreture']),\
			self.weather['tempreture_unit'],self.weather['client_ip'],self.weather['user_name'])
		db.session.add(a_history)
		if len(self.read_weather(self.weather['city_name'])) > 0:
			self.update_weather(self.weather)
		else:
			self.insert_weather()

	def read_weather(self,city_name=None):
		"""read weather table"""
		row = []
		if city_name != None:
			local_data = Weather.query.filter_by(city=city_name).all()
		else:
			local_data = Weather.query.all()
		for r in local_data:
			row.append('No.'+str(r.id)+' City: '+r.city+' Weather: '+r.weather_status+' Tempreture: '+str(r.tempreture)+''+r.tempreture_unit)
		return row

	def update_weather(self,weather):
		"""update weather table"""
		w = Weather.query.filter_by(city=weather['city_name']).first()
		w.weather_status = weather['status']
		w.tempreture = weather['tempreture']
		w.tempreture_unit = weather['tempreture_unit']
		db.session.add(w)

	def insert_weather(self):
		"""insert record into weather table"""
		insert_a_record = Weather(self.weather['city_name'],self.weather['status'],int(self.weather['tempreture']),self.weather['tempreture_unit'])
		db.session.add(insert_a_record)

	def show_history(self):
		"""get query history from database"""
		history = []
		history_query = History.query.all()
		for his in history_query:
			history.append([his.city,his.weather_status,his.query_utc_time,\
				str(his.tempreture),his.tempreture_unit,his.user_name,his.client_ip])
		return history

	def show_help(self):
		"""show help infomation"""
		help_info = ['输入 城市名，可获取城市的天气;','单击 帮助 按钮，获取帮助文档;',\
		'单击 历史 按钮，获取查询历史;','单击 更正 按钮，可以进入更正页面修改本地数据库数据。']
		return help_info