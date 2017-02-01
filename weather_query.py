# coding:utf-8
import requests

class ThinkPage(object):
	"""心知天气接口类"""
	def __init__(self):
		self.weather_string = 'https://api.thinkpage.cn/v3/weather/now.json?location=city_name&language=zh-Hans&unit=c&key='
		self.life_string = 'https://api.thinkpage.cn/v3/life/suggestion.json?location=city_name&language=zh-Hans&key='
		self.key_string = 'xxob9t1ag7zpdv91'

	def get_weather_from_api(self,city_name):
		"""从接口获取天气数据"""	
		url = self.weather_string.replace('city_name',city_name).strip() + self.key_string.strip()
		res = requests.get(url)
		if res.status_code != 200:
			return None
		res_dict = res.json()
		return res_dict

	def get_life_from_api(self,city_name):
		"""从接口获取生活指数数据"""	
		url = self.life_string.replace('city_name',city_name).strip() + self.key_string.strip()
		res = requests.get(url)
		if res.status_code != 200:
			return None
		res_dict = res.json()
		return res_dict

	# def query_weather(self,city_name):
	# 	"""获取最新城市天气状况"""
	# 	weather_data = self.get_weather_from_api(city_name)
	# 	if weather_data == None: return None
	# 	return weather_data

	# def query_life(self,city_name):
	# 	"""获取最新城市生活指数"""
	# 	life_data = self.get_life_from_api(city_name)
	# 	if life_data == None: return None
	# 	return life_data