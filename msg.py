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

def reply(msg_xml,content):
	rec_msg = parse_msg(msg_xml)
	to_user_name = rec_msg['ToUserName']
	from_user_name = rec_msg['FromUserName']
	reply_msg = """<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content></xml>"""
	creat_time =int(time.time())
	echostr = reply_msg % (to_user_name,from_user_name,creat_time,'text',content)
	# print(type(echostr))
	# print(echostr)
	if content != None:
		return echostr
	else:
		return 'success'
