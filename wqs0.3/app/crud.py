# coding:utf-8

from .models import Weather, History


def read_help():
	help = 'Input a city name ,get it\'s weather;','Click help button, get help doc',\
		'Click history button, get query history;','Click modify button ,ready to update data.'
	return help

def read_history():
	"""read history table"""
	history = []
	history_query = History.query.all()

	for his in history_query:
		history.append([his.city,his.weather_status,his.query_utc_time,\
			str(his.tempreture),his.tempreture_unit,his.user_name,his.client_ip])
	return history	

def insert_history(weather_dict):
	"""insert a record into history table"""
	weather = weather_dict
	insert_a_record =  History(weather['city_name'],weather['weather_status'],weather['query_utc_datetime'],\
		int(weather['tempreture']),weather['tempreture_unit'],weather['client_ip'],weather['user_name'])

	db.session.add(insert_a_record)

def read_weather(weather_dict):
	"""read weather table"""
	row = []
	weather = weather_dict
	if weather['city_name'] != None:
		local_data = Weather.query.filter_by(city_name=weather['city_name']).all()
	else:
		local_data = Weather.query.all()

	for r in local_data:
		row.append('序号: '+str(r.id)+' 城市名: '+r.city+' 天气状况: '+r.weather_status+' 温度: '+str(r.tempreture)+''+r.tempreture_unit)
	return row

def update_weather(weather_dict):
	"""update weather table"""
	weather = weather_dict
	update_object = Weather.query.filter_by(city_name=weather['city_name']).first()
	update_object.weather_status = weather['weather_status']
	update_object.tempreture = weather['tempreture']
	update_object.tempreture_unit = weather['tempreture_unit']
	db.session.add(update_object)

def insert_weather(weather_dict):
	"""insert record into weather table"""
	weather = weather_dict
	insert_a_record = Weather(weather['city_name'],weather['weather_status'],int(weather['tempreture']),weather['tempreture_unit'])
	db.session.add(insert_a_record)
	