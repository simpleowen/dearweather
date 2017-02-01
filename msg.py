# coding:utf-8
import xml.etree.ElementTree as ET
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
	rec_msg = parse_msg(msg_xml)
	reply_msg = u"""<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content></xml>"""
	echostr = reply_msg % (rec_msg['ToUserName'],rec_msg['FromUserName'],rec_msg['CreateTime'],rec_msg['MsgType'],text)
	return echostr
