# coding:utf-8
import requests

class ThinkPage(object):
	"""心知天气接口"""
	def __init__(self):
		self.weather_string = 'https://api.thinkpage.cn/v3/weather/now.json?location=city_name&language=zh-Hans&unit=c&key='
		self.life_string = 'https://api.thinkpage.cn/v3/life/suggestion.json?location=city_name&language=zh-Hans&key='
		self.key_string = 'xxob9t1ag7zpdv91'

	def get_weather_from_api(self,city_name):
		"""天气数据"""	
		url = self.weather_string.replace('city_name',city_name).strip() + self.key_string.strip()
		res = requests.get(url)
		if res.status_code != 200:
			return None
		res_dict = res.json()
		return res_dict

	def get_life_from_api(self,city_name):
		"""生活指数数据"""	
		url = self.life_string.replace('city_name',city_name).strip() + self.key_string.strip()
		res = requests.get(url)
		if res.status_code != 200:
			return None
		res_dict = res.json()
		return res_dict
