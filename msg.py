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
	if msg['Content'] == '历史':
		content = crud.show_history()
		# return content
	elif msg['Content'] == '帮助':
		content = '输入 城市名，可获取城市的天气;','单击 帮助 按钮，获取帮助文档;',\
		'单击 历史 按钮，获取查询历史;','单击 更正 按钮，可以进入更正页面修改本地数据库数据。'
		# return content
	else:
		weather_data = tp.get_weather_from_api(msg['Content'])
		life_data = tp.get_life_from_api(msg['Content'])
		if weather_data == None: 
			content = '没有找到该城市'
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
			"\n温度：" + weather_data['results'][0]['now']['temperature'] + "度"+ "," + \
			"\n紫外线强度：" + life_data['results'][0]['suggestion']['uv']['brief']+ "," + \
			"\n穿衣：" + life_data['results'][0]['suggestion']['dressing']['brief']+ "," + \
			"\n运动：" + life_data['results'][0]['suggestion']['sport']['brief']+ "," + \
			"\n感冒：" + life_data['results'][0]['suggestion']['flu']['brief']+ "," + \
			"\n旅游：" + life_data['results'][0]['suggestion']['travel']['brief']+ "," + \
			"\n洗车：" + life_data['results'][0]['suggestion']['car_washing']['brief']+ "," + \
			"\n数据更新时间：" + life_data['results'][0]['last_update']
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
