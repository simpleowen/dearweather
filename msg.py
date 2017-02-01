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
	weather_data = tp.query_weather(msg['Content'])
	return weather_data

def reply(msg_xml,text):
	# rec_msg = parse_msg(msg_xml)
	reply_msg = \
	u"""
	<xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[%s]]></MsgType>
	<Content><![CDATA[%s]]></Content>
	</xml>
	"""
	creat_time =int(time.time())
	echostr = reply_msg % ('ToUserName','FromUserName',creat_time,'text',text)
	echostr = echostr.encode(encoding='utf-8')
	# print(type(echostr))
	# print(echostr)
	if text != None:
		return echostr
	else:
		return 'success'
