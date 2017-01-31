# coding:utf-8
import requests

class ThinkPage(object):
	"""心知天气接口类"""
	def __init__(self):
		self.call_string = 'https://api.thinkpage.cn/v3/weather/now.json?location=city_name&language=zh-Hans&unit=c&key='
		self.key_string = 'xxob9t1ag7zpdv91'

	def get_data_from_api(self,city_name):
		"""从接口获取天气数据"""	
		url = self.call_string.replace('city_name',city_name).strip() + self.key_string.strip()
		res = requests.get(url)
		if res.status_code != 200:
			return None
		res_dict = res.json()
		return res_dict

	def query_weather(self,city_name):
		"""获取最新城市天气状况"""
		weather_data = self.get_data_from_api(city_name)
		if weather_data == None: return None
		return weather_data
