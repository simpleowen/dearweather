# coding:utf-8
import xml.etree.ElementTree as ET
import time
from weather_query import ThinkPage as TP
from orm import CRUD

def parse_msg(msg_xml):
	root = ET.fromstring(msg_xml)
	msg = {}
	for child in root:
		msg[child.tag] = child.text
	return msg

def rec(msg_xml):
	tp = TP()
	crud = CRUD()
	msg = parse_msg(msg_xml)
	if msg['Content'] == 'History':
		content = crud.show_history()
		# return content
	elif msg['Content'] == 'Help':
		content = 'Input a city name ,get it\'s weather;','Click help button, get help doc',\
		'Click history button, get query history;','Click modify button ,ready to update data.'
		# return content
	else:
		weather_data = tp.get_weather_from_api(msg['Content'])
		life_data = tp.get_life_from_api(msg['Content'])
		if weather_data == None: 
			content = 'No found the city'
			return content
		else:
			query_datetime = datetime.datetime.utcnow()
			weather = {}
			weather['status'] = weather_data['results'][0]['now']['text']
			weather['tempreture'] = weather_data['results'][0]['now']['temperature']
			weather['city_name'] = weather_data['results'][0]['location']['name']
			weather['client_ip'] = ''
			weather['query_utc_datetime'] = query_datetime
			weather['tempreture_unit'] = 'C'
			weather['user_name'] = 'WEIXIN'
			crud.save_to_db(weather) 
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
			# return content
	return content

def reply(msg_xml,content):
	rec_msg = parse_msg(msg_xml)
	to_user_name = rec_msg['ToUserName']
	from_user_name = rec_msg['FromUserName']
	reply_msg = """<xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[%s]]></MsgType>
	<Content><![CDATA[%s]]></Content>
	</xml>"""
	create_time =int(time.time())
	echostr = reply_msg % (from_user_name,to_user_name,create_time,'text',content)
	if content != None:
		return echostr
	else:
		return 'success'
