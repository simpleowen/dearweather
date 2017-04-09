# coding:utf-8
import hashlib
import xml.etree.ElementTree as ET
import datetime
import time
from .weather_api import ThinkPage as TP
from .crud import read_help, read_history, insert_history, read_weather, update_weather, insert_weather

def identify_wechat(signature,timestamp,nonce,echostr):
	"""微信认证"""
	temparr = []
	token = "dearweather"
	temparr = [token,timestamp,nonce]
	temparr.sort()
	newstr = "".join(temparr)
	sha1str = hashlib.sha1(newstr.encode('utf-8'))
	temp = sha1str.hexdigest()
	if signature == temp:
		return echostr
	else:
		return 'False'

def parse_msg(msg_xml):
	"""解析微信消息"""
	root = ET.fromstring(msg_xml)
	msg_weixin = {}
	for child in root:
		msg_weixin[child.tag] = child.text # str
	return msg_weixin

def handle_wechat(msg_xml):
	"""接收微信消息并返回"""

	msg_user = parse_msg(msg_xml) 

	if msg_user['Content'] in ['History', 'history', '历史']:
		content = read_history()

	elif msg_user['Content'] in ['Help', 'help', '帮助']:
		content = read_help()

	else:
		tp = TP()
		weather_data = tp.get_weather_from_api(msg_user['Content'].decode('utf-8'))
		life_data = tp.get_life_from_api(msg_user['Content'].decode('utf-8'))

		if weather_data == None: 
			content = 'no city named like ' + msg_user['Content']
		else:
			query_datetime = datetime.datetime.utcnow()
			weather = {}
			weather['weather_status'] = weather_data['results'][0]['now']['text']
			weather['tempreture'] = weather_data['results'][0]['now']['temperature']
			weather['city_name'] = weather_data['results'][0]['location']['name']
			weather['client_ip'] = ''
			weather['query_utc_datetime'] = query_datetime
			weather['tempreture_unit'] = 'C'
			weather['user_name'] = 'WEIXIN'

			content = weather_data['results'][0]['location']['name'] + " " + \
				weather_data['results'][0]['now']['text'] + "," + \
				"\nTempreture:" + weather_data['results'][0]['now']['temperature'] + "度"+ "," + \
				"\nUV:" + life_data['results'][0]['suggestion']['uv']['brief']+ "," + \
				"\nDressing:" + life_data['results'][0]['suggestion']['dressing']['brief']+ "," + \
				"\nSport:" + life_data['results'][0]['suggestion']['sport']['brief']+ "," + \
				"\nFlu:" + life_data['results'][0]['suggestion']['flu']['brief']+ "," + \
				"\nTravel:" + life_data['results'][0]['suggestion']['travel']['brief']+ "," + \
				"\nCar_washing:" + life_data['results'][0]['suggestion']['car_washing']['brief']+ "," + \
				"\nlast_update:" + life_data['results'][0]['last_update']

	to_user_name = msg_user['ToUserName']
	from_user_name = msg_user['FromUserName']
	create_time =int(time.time())

	reply_msg = """<xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[%s]]></MsgType>
	<Content><![CDATA[%s]]></Content>
	</xml>"""

	echostr = reply_msg % (from_user_name,to_user_name,create_time,'text',content)

	if len(read_weather(weather)) > 0:
		update_weather(weather)
	else:
		insert_weather(weather)

	insert_history(weather)

	return echostr
