# coding:utf-8
import requests
import time
import datetime
from app.models import Weather,History


class ThinkPage(object):
	"""thinkpage api"""

	def __init__(self):
		self.weather_string = 'https://api.thinkpage.cn/v3/weather/now.json?location=city_name&language=zh-Hans&unit=c&key='
		self.life_string = 'https://api.thinkpage.cn/v3/life/suggestion.json?location=city_name&language=zh-Hans&key='
		self.key_string = 'xxob9t1ag7zpdv91'
		self.copyright = 'data from http://www.thinkpage.cn'

	def get_weather_from_api(self,city_name):
		"""Weather data"""	
		print(city_name)
		url = self.weather_string.replace('city_name',city_name).strip() + self.key_string.strip()
		res = requests.get(url)

		if res.status_code != 200:
			return None
		res_dict = res.json()

		return res_dict

	def get_life_from_api(self,city_name):
		"""life data"""	
		url = self.life_string.replace('city_name',city_name).strip() + self.key_string.strip()
		res = requests.get(url)
		if res.status_code != 200:
			return None
		res_dict = res.json()
		return res_dict


class BaiduMap(object):
	"""百度地图接口"""
	def __init__(self):
		self.copyright = '数据来自百度地图http://map.baidu.com'
		self.baidu_ip_api_str = 'http://api.map.baidu.com/location/ip?ak=gQL47dOSa0Ft8oCUvr1h6XgLLUFYFX2U&coor=bd09ll&ip=client_ip'
		self.baidu_timezone_api_str = 'http://api.map.baidu.com/timezone/v1?coord_type=bd09ll&location=x_y&timestamp=unix_time&ak=gQL47dOSa0Ft8oCUvr1h6XgLLUFYFX2U'

	def ip_to_timezone(self,client_ip):
		"""根据IP获取经纬度数据，进而获取时区"""
		ip_str = self.baidu_ip_api_str.replace('client_ip',client_ip)
		res_x_y = requests.get(ip_str).json()
		if res_x_y['status'] == 0:
			x = res_x_y['content']['point']['x']
			y = res_x_y['content']['point']['y']
			timestamp = int(time.time())
			location = str(y)+","+str(x)
			timezone_url = self.baidu_timezone_api_str.replace('x_y',location).replace('unix_time',str(timestamp))
			res_timezone = requests.get(timezone_url).json()
			if res_timezone['status'] == 0:
				return res_timezone['timezone_id']
			else:
				# print('no timezone data')
				return None
		else:
			# print('no coordinates data')
			return None

