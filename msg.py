# coding:utf-8
import xml.etree.ElementTree as ET
import time
from weather_query import ThinkPage as TP

def parse_msg(msg_xml):
	root = ET.fromstring(msg_xml)
	msg = {}
	for child in root:
		msg[child.tag] = child.text
	return msg

def rec(msg_xml):
	tp = TP()
	msg = parse_msg(msg_xml)
	weather_data = tp.get_weather_from_api(msg['Content'])
	life_data = tp.get_life_from_api(msg['Content'])
	if weather_data == None: 
		content = '没有找到该城市'.decode('utf-8')
		return content
	else:
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
	creat_time =int(time.time())
	echostr = reply_msg % (from_user_name,to_user_name,creat_time,'text',content)
	if content != None:
		return echostr
	else:
		return 'success'
